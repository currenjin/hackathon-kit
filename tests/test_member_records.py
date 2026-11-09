"""Real CLI persistence checks with synthetic data; no native host UI exercised."""
import argparse
import importlib.util
import json
import os
from unittest import mock
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / 'tools/member_records.py'


class MemberRecords(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR'))
        self.addCleanup(self.tmp.cleanup)
        self.event = Path(self.tmp.name).resolve() / 'synthetic-event'
        self.event.mkdir()

    def run_cli(self, action, *args, ok=True, event=None):
        result = subprocess.run([sys.executable, '-B', str(CLI), str(event or self.event),
                                 action, *args], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0 if ok else 2, result.stderr)
        if not ok:
            self.assertIn('member-records:', result.stderr)
        return json.loads(result.stdout) if ok else result.stderr

    def register(self, member='alice', role='프론트엔드 개발', **kw):
        return self.run_cli('register', '--member', member, '--identity', member,
                            '--role', role, '--confirmed', '--identity-source',
                            'safe-alias-confirmed', '--role-source', 'native-freeform', **kw)

    def test_no_records_read_does_not_create_directory(self):
        self.assertEqual(self.run_cli('list'), [])
        self.assertEqual(list(self.event.iterdir()), [])

    def test_two_members_custom_role_and_provenance(self):
        self.register()
        self.register('bob', '데이터 분석 / 발표')
        records = self.run_cli('list')
        self.assertEqual([r['member_id'] for r in records], ['alice', 'bob'])
        self.assertEqual(records[1]['main_role'], '데이터 분석 / 발표')
        self.assertEqual(records[1]['author'], 'bob')
        self.assertEqual(records[1]['role_source'], 'native-freeform')
        self.assertTrue(records[1]['confirmed_at'].endswith('+00:00'))

    def test_selection_is_read_only_and_identity_must_match(self):
        self.register()
        before = (self.event / 'members/alice.yaml').read_bytes()
        self.run_cli('read', '--member', 'alice', '--identity', 'alice')
        self.run_cli('read', '--member', 'alice', '--identity', 'bob', ok=False)
        self.assertEqual(before, (self.event / 'members/alice.yaml').read_bytes())

    def test_duplicate_and_case_alias_rejected(self):
        self.register()
        self.register(ok=False)
        self.register('Alice', ok=False)
        self.assertEqual(len(self.run_cli('list')), 1)

    def test_cancel_empty_or_unconfirmed_has_no_write(self):
        self.run_cli('register', '--member', 'alice', '--identity', 'alice',
                     '--role', '프론트엔드 개발', ok=False)
        self.register(role='', ok=False)
        self.assertEqual(list(self.event.iterdir()), [])

    def test_explicit_role_update_preserves_other_member_and_history(self):
        self.register()
        self.register('bob', '백엔드 개발')
        other = (self.event / 'members/bob.yaml').read_bytes()
        args = ['--member', 'alice', '--identity', 'alice', '--role', '발표',
                '--role-source', 'conversation', '--expected-role', '프론트엔드 개발']
        self.run_cli('update', *args, ok=False)
        record = self.run_cli('update', *args, '--confirmed')
        self.assertEqual(record['main_role'], '발표')
        self.assertEqual(record['history'][0]['main_role'], '프론트엔드 개발')
        self.run_cli('update', *args, '--confirmed', ok=False)
        self.assertEqual(other, (self.event / 'members/bob.yaml').read_bytes())

    def test_event_isolation_and_missing_selection(self):
        self.register()
        second = self.event.parent / 'second-event'
        second.mkdir()
        self.run_cli('read', '--member', 'alice', '--identity', 'alice', event=second, ok=False)
        self.register('alice', '백엔드 개발', event=second)
        self.assertEqual(self.run_cli('read', '--member', 'alice', '--identity', 'alice')['main_role'], '프론트엔드 개발')

    def test_literal_identifiers_rejected_before_io(self):
        for member in ['../escape', 'a/b', '.', 'ALICE', 'a.yaml', 'a\\b', 'a\n']:
            with self.subTest(member=member):
                self.register(member, ok=False)
        self.assertEqual(list(self.event.iterdir()), [])

    def test_symlink_directory_and_member_rejected(self):
        outside = self.event.parent / 'outside'
        outside.mkdir()
        (self.event / 'members').symlink_to(outside, target_is_directory=True)
        self.register(ok=False)
        self.run_cli('list', ok=False)
        self.assertEqual(list(outside.iterdir()), [])
        (self.event / 'members').unlink()
        self.register()
        (self.event / 'members/bob.yaml').symlink_to(self.event / 'members/alice.yaml')
        self.run_cli('read', '--member', 'bob', '--identity', 'bob', ok=False)
        self.register('bob', ok=False)

    def test_symlink_event_and_traversal_path_rejected(self):
        alias = self.event.parent / 'alias'
        alias.symlink_to(self.event, target_is_directory=True)
        self.register(event=alias, ok=False)
        self.register(event=str(self.event) + '/../synthetic-event', ok=False)
        self.assertEqual(list(self.event.iterdir()), [])

    def test_interrupted_publication_remains_readable_without_mutation(self):
        self.register('bob', '백엔드 개발')
        script = (
            "import importlib.util,os,sys\n"
            "spec=importlib.util.spec_from_file_location('member_cli',sys.argv[1])\n"
            "module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)\n"
            "original_link=module.os.link\n"
            "def interrupt_after_publication(*args,**kwargs):\n"
            "    original_link(*args,**kwargs)\n"
            "    os._exit(73)\n"
            "module.os.link=interrupt_after_publication\n"
            "sys.argv=[sys.argv[1],sys.argv[2],'register','--member','alice',"
            "'--identity','alice','--role','프론트엔드 개발','--identity-source',"
            "'safe-alias-confirmed','--role-source','native-choice','--confirmed']\n"
            "module.main()\n"
        )
        result = subprocess.run([sys.executable, '-B', '-c', script,
                                 str(CLI), str(self.event)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 73, result.stderr)
        members = self.event / 'members'
        self.assertEqual((members / 'alice.yaml').stat().st_nlink, 2)
        before = {p.name: p.read_bytes() for p in members.iterdir()}
        self.assertEqual([r['member_id'] for r in self.run_cli('list')], ['alice', 'bob'])
        record = self.run_cli('read', '--member', 'alice', '--identity', 'alice')
        self.assertEqual(record['main_role'], '프론트엔드 개발')
        self.assertEqual(before, {p.name: p.read_bytes() for p in members.iterdir()})
        self.register('alice', ok=False)
        self.assertEqual(before, {p.name: p.read_bytes() for p in members.iterdir()})

    def test_external_hardlinks_are_rejected(self):
        self.register()
        os.link(self.event / 'members/alice.yaml', self.event.parent / 'external-alias')
        self.run_cli('read', '--member', 'alice', '--identity', 'alice', ok=False)
        self.run_cli('list', ok=False)

    def test_unavailable_posix_backend_explains_wsl_without_writing(self):
        script = (
            "import runpy,sys; sys.modules['fcntl']=None; "
            "sys.argv=[sys.argv[1],sys.argv[2],'list']; "
            "runpy.run_path(sys.argv[0],run_name='__main__')"
        )
        result = subprocess.run([sys.executable, '-B', '-c', script,
                                 str(CLI), str(self.event)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('WSL', result.stderr)
        self.assertNotIn('Traceback', result.stderr)
        self.assertEqual(list(self.event.iterdir()), [])

    def test_failed_registration_never_publishes_partial_record(self):
        self.register('bob', '백엔드 개발')
        other = (self.event / 'members/bob.yaml').read_bytes()
        spec = importlib.util.spec_from_file_location('member_records_under_test', CLI)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        args = argparse.Namespace(action='register', event=str(self.event),
                                  member='alice', identity='alice', role='프론트엔드 개발',
                                  confirmed=True, identity_source='safe-alias-confirmed',
                                  role_source='native-choice', expected_role=None)

        def interrupted_dump(record, stream, **kwargs):
            stream.write('{"member_id": "alice",')
            raise OSError('injected partial serialization failure')

        with mock.patch.object(module.json, 'dump', side_effect=interrupted_dump):
            with self.assertRaisesRegex(OSError, 'injected'):
                module.perform(args)
        self.assertFalse((self.event / 'members/alice.yaml').exists())
        self.assertEqual([p.name for p in (self.event / 'members').iterdir()], ['bob.yaml'])
        self.assertEqual(self.run_cli('list')[0]['member_id'], 'bob')
        self.assertEqual(other, (self.event / 'members/bob.yaml').read_bytes())
        self.register('alice')
        self.assertEqual(len(self.run_cli('list')), 2)

    def test_tampered_canonical_identity_rejected(self):
        self.register()
        path = self.event / 'members/alice.yaml'
        data = json.loads(path.read_text())
        data['member_id'] = 'bob'
        path.write_text(json.dumps(data))
        self.run_cli('read', '--member', 'alice', '--identity', 'alice', ok=False)


if __name__ == '__main__':
    unittest.main()
