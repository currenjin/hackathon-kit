"""Member record persistence for init/onboard. JSON is a YAML-compatible subset.

Host commands confirm event policy and respondent identity before invoking this CLI.
This is not authentication. No session binding is written to disk.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
try:
    import fcntl
except ImportError:
    fcntl = None
import json
import os
from pathlib import Path
import re
import stat
import sys
import uuid


IDENTIFIER = re.compile(r'[a-z0-9](?:[a-z0-9-]{0,37}[a-z0-9])?\Z')
DIR_FLAGS = os.O_RDONLY | getattr(os, 'O_DIRECTORY', 0) | getattr(os, 'O_NOFOLLOW', 0)


def identifier(value):
    if not value or not IDENTIFIER.fullmatch(value) or '--' in value:
        raise ValueError('Use a confirmed lowercase handle or safe alias (1–39 characters).')
    return value


@contextmanager
def event_directory(path):
    # Walk from / with no-follow descriptors, including every ancestor.
    if '..' in Path(path).parts:
        raise ValueError('Parent traversal is not allowed.')
    parts = Path(os.path.abspath(path)).parts
    fd = os.open(parts[0], DIR_FLAGS)
    try:
        for part in parts[1:]:
            child = os.open(part, DIR_FLAGS, dir_fd=fd)
            os.close(fd)
            fd = child
        yield fd
    finally:
        os.close(fd)


def read_record(fd, member):
    name = identifier(member) + '.yaml'
    record_fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
    with os.fdopen(record_fd) as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode):
            raise ValueError('Member record must be a regular file.')
        if info.st_nlink != 1:
            # A process can stop after publishing the complete record but before
            # removing its staging name. Accept only aliases accounted for here.
            local_links = 1
            for candidate in os.listdir(fd):
                if not re.fullmatch(r'\.member-[0-9a-f]{32}', candidate):
                    continue
                try:
                    alias = os.stat(candidate, dir_fd=fd, follow_symlinks=False)
                except FileNotFoundError:
                    continue
                if (stat.S_ISREG(alias.st_mode)
                        and (alias.st_dev, alias.st_ino) == (info.st_dev, info.st_ino)):
                    local_links += 1
            if local_links != info.st_nlink:
                raise ValueError('Member record has an unaccounted hard link.')
        record = json.load(stream)
    if (not isinstance(record, dict) or record.get('member_id') != member
            or record.get('author') != member or not record.get('main_role')):
        raise ValueError('Canonical member identity or role does not match.')
    return record


def perform(args):
    if (fcntl is None or not hasattr(os, 'O_DIRECTORY')
            or not hasattr(os, 'O_NOFOLLOW')):
        raise ValueError('Team member storage requires macOS or Linux. On Windows, '
                         'run the kit and this Python CLI inside WSL; see '
                         'references/team-participation.md#실행-환경.')
    writing = args.action in ('register', 'update')
    if args.action != 'list':
        identifier(args.member)
        if identifier(args.identity) != args.member:
            raise ValueError('Confirmed respondent must match the selected member.')
    if writing:
        if not args.confirmed or not args.role or not args.role.strip() or not args.role_source:
            raise ValueError('An explicit role answer/approval and provenance are required.')
        if args.action == 'register' and not args.identity_source:
            raise ValueError('Confirmed identity provenance is required.')
        if args.action == 'update' and not args.expected_role:
            raise ValueError('The previously read role is required.')
    with event_directory(args.event) as event_fd:
        try:
            members_fd = os.open('members', DIR_FLAGS, dir_fd=event_fd)
        except FileNotFoundError:
            if args.action == 'list':
                return []
            if args.action != 'register':
                raise
            try:
                os.mkdir('members', dir_fd=event_fd)
            except FileExistsError:
                pass
            members_fd = os.open('members', DIR_FLAGS, dir_fd=event_fd)
        try:
            fcntl.flock(members_fd, fcntl.LOCK_EX if writing else fcntl.LOCK_SH)
            names = os.listdir(members_fd)
            if args.action == 'list':
                return [read_record(members_fd, name[:-5]) for name in sorted(names)
                        if name.endswith('.yaml')]
            name = args.member + '.yaml'
            if any(n.casefold() == name.casefold() and n != name for n in names):
                raise ValueError('Case-alias member collision.')
            if args.action == 'read':
                return read_record(members_fd, args.member)
            now = datetime.now(timezone.utc).isoformat()
            if args.action == 'register':
                record = dict(member_id=args.member, author=args.identity,
                              main_role=args.role, identity_source=args.identity_source,
                              role_source=args.role_source, confirmed_at=now, history=[])
                # Publish only a fully serialized record. link is atomic and refuses
                # an existing target, unlike replace; the directory lock protects readers.
                temp = '.member-' + uuid.uuid4().hex
                try:
                    target = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                                     0o644, dir_fd=members_fd)
                    with os.fdopen(target, 'w') as stream:
                        json.dump(record, stream, ensure_ascii=False, indent=2)
                        stream.write('\n')
                        stream.flush()
                        os.fsync(stream.fileno())
                    os.link(temp, name, src_dir_fd=members_fd,
                            dst_dir_fd=members_fd, follow_symlinks=False)
                finally:
                    try:
                        os.unlink(temp, dir_fd=members_fd)
                    except FileNotFoundError:
                        pass
            else:
                record = read_record(members_fd, args.member)
                if record['main_role'] != args.expected_role:
                    raise ValueError('Role changed since confirmation; read and confirm again.')
                record['history'].append({k: record[k] for k in
                                          ('main_role', 'role_source', 'confirmed_at')})
                record.update(main_role=args.role, role_source=args.role_source, confirmed_at=now)
                temp = '.member-' + uuid.uuid4().hex
                try:
                    target = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                                     0o644, dir_fd=members_fd)
                    with os.fdopen(target, 'w') as stream:
                        json.dump(record, stream, ensure_ascii=False, indent=2)
                        stream.write('\n')
                    os.replace(temp, name, src_dir_fd=members_fd, dst_dir_fd=members_fd)
                finally:
                    try:
                        os.unlink(temp, dir_fd=members_fd)
                    except FileNotFoundError:
                        pass
            return record
        finally:
            os.close(members_fd)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('event', help='Existing event directory; no symlink components')
    parser.add_argument('action', choices=['list', 'read', 'register', 'update'])
    parser.add_argument('--member')
    parser.add_argument('--identity')
    parser.add_argument('--role')
    parser.add_argument('--expected-role')
    parser.add_argument('--confirmed', action='store_true')
    parser.add_argument('--identity-source', choices=['github-confirmed', 'safe-alias-confirmed'])
    parser.add_argument('--role-source', choices=['native-choice', 'native-freeform', 'conversation'])
    args = parser.parse_args()
    try:
        result = perform(args)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print('member-records: ' + str(error), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
