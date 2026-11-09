"""Static command propagation/branch contracts, not native interactive E2E."""
from pathlib import Path
import re
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text()


class ParticipationContracts(unittest.TestCase):
    def test_every_command_reaches_member_policy(self):
        for command in (ROOT / '.claude/commands').glob('*.md'):
            self.assertIn('references/workflow-policy.md', command.read_text(), command.name)
        for path in ['AGENTS.md', 'CLAUDE.md', 'references/workflow-policy.md']:
            self.assertIn('references/team-participation.md' if path != 'references/workflow-policy.md'
                          else 'team-participation.md', read(path))
        self.assertIn('매 command', read('references/team-participation.md'))

    def test_init_mode_then_team_only_role(self):
        body = read('.claude/commands/init.md')
        self.assertIn('이번 해커톤은 어떻게 참가하나요?', body)
        self.assertIn('개인 / 팀', body)
        self.assertIn('개인은 역할 질문을 건너뛴다', body)
        self.assertIn('참가 방식 응답 뒤', body)
        self.assertIn('이번 팀에서 주로 맡을 역할은 무엇인가요?', read('references/team-participation.md'))
        data = yaml.safe_load(read('templates/hackathon.yaml'))
        self.assertEqual(data['participation']['mode'], 'unknown')
        self.assertNotIn('current_member', data['participation'])
        self.assertNotIn('main_role', data['participation'])

    def test_onboard_existing_new_empty_and_historical_branches(self):
        body = read('.claude/commands/onboard.md')
        for text in ['이번 팀에 본인의 주 역할을 이미 등록했나요?', '예, 등록했어요',
                     '아니요, 처음 등록해요', '본인에 해당하는 팀원 기록을 선택하세요.',
                     '<member-id> (<main-role>)', '내 기록이 없어요', '기록이 없으면',
                     '종료된 행사', '신규 본인 등록', '기존 기록 선택']:
            self.assertIn(text, body)

    def test_native_surface_and_cancellation_contract(self):
        body = read('references/team-participation.md')
        for text in ['AskUserQuestion', 'request_user_input', '2–3', 'native Other',
                     '프론트엔드 개발', '백엔드 개발', '같은 질문', '페이지',
                     '취소', '빈 응답', '모드 전환', '대화형', '직접 입력']:
            self.assertIn(text, body)

    def test_session_identity_legacy_and_priority(self):
        body = read('references/team-participation.md')
        for text in ['세션 안에서만', '매 command', '정본', '우선순위', '다른 역할',
                     'git 이름·이메일', '응답자', '누락', 'unknown', '일괄 migration',
                     '읽기 전용', '자동 변경하지 않는다', '포인터 파일을 만들지 않는다']:
            self.assertIn(text, body)

    def test_helper_is_on_documented_command_path(self):
        body = read('references/team-participation.md')
        for text in ['tools/member_records.py', ' register ', ' read ', ' list',
                     ' update ', '--expected-role', '--confirmed', '--identity',
                     'native-freeform', 'conversation', 'JSON', 'symlink']:
            self.assertIn(text, body)
        for name in ['init', 'onboard']:
            self.assertIn('team-participation.md', read('.claude/commands/' + name + '.md'))

    def test_bilingual_sharing_and_links(self):
        for name in ['README.md', 'README.en.md']:
            body = read(name)
            self.assertIn('Use this template', body)
            self.assertIn('references/team-participation.md', body)
        for name in ['README.md', 'README.en.md', 'AGENTS.md', 'CLAUDE.md',
                     'references/team-participation.md', 'references/workflow-policy.md']:
            for link in re.findall(r'\]\(([^)]+)\)', read(name)):
                if '://' not in link and not link.startswith('#'):
                    self.assertTrue((ROOT / name).parent.joinpath(link.split('#')[0]).exists(), link)


if __name__ == '__main__':
    unittest.main()
