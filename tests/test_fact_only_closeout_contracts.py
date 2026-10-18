"""Static policy regression checks, not live LLM behavior verification.

Run with the existing suite: python3 -B -m unittest discover -s tests -v
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(relative):
    return (ROOT / relative).read_text(encoding='utf-8')


class FactOnlyCloseoutContracts(unittest.TestCase):
    def test_shared_policy_covers_absence_refusal_and_source_preservation(self):
        body = read('AGENTS.md')
        for required in ['사실 기반 작업 회고', '결과·발표 사용자 보고',
                         '소감·감정·감사·성장·개인적인 의미', '필수 인터뷰',
                         '입력이 없거나 사용자가 거절해도', '빈 감상 섹션',
                         'reflection_pending', '대기·부분완료로 낮추지 않는다',
                         '미확인', '비해당', '별도 source', '별도 요청']:
            with self.subTest(required=required):
                self.assertIn(required, body)

    def test_both_entrypoints_apply_shared_fact_only_completion(self):
        for command in ['retro', 'archive']:
            body = read(f'.claude/commands/{command}.md')
            with self.subTest(command=command):
                for required in ['사실 기반 작업 회고', 'field-status-and-closeout.md',
                                 '소감 입력은 완료 조건이 아니다', '필수 인터뷰',
                                 'reflection_pending', '대기·부분완료로 낮추지 않는다']:
                    self.assertIn(required, body)

    def test_retro_has_factual_inputs_and_no_legacy_personal_roles(self):
        body = read('.claude/commands/retro.md')
        for required in ['기존 workspace', 'evidence', '결과·발표 사용자 보고',
                         '결정과 근거', '실행·검증', '확인된 문제', '미검증', '후속작업']:
            self.assertIn(required, body)
        routing = read('references/model-routing.md')
        self.assertNotIn('Claude + 사용자', routing)
        self.assertNotIn('소감과 교훈(사용자가 말한 것만)', routing)
        self.assertIn('사실 기록 정리', routing)

    def test_archive_and_completion_source_separate_records_from_shutdown(self):
        for relative in ['.claude/commands/archive.md',
                         'references/field-status-and-closeout.md',
                         'references/workflow-policy.md']:
            with self.subTest(file=relative):
                body = read(relative)
                self.assertIn('기록 완료와 운영 종료', body)
                self.assertIn('소감', body)
                self.assertIn('미확인', body)
        self.assertIn('링크·상태·결과', read('.claude/commands/archive.md'))

    def test_existing_safety_and_history_boundaries_remain(self):
        for command in ['retro', 'archive']:
            body = read(f'.claude/commands/{command}.md')
            with self.subTest(command=command):
                for required in ['사용자가 대상 행사를 확인한 뒤', '소유 경계',
                                 '과거 규칙·선택·제작 시각·evidence·oracle 격리·실제 제출 이력',
                                 '현재 사용자의 게시 금지·보호 경로', '승인 없이 자동 실행하지 않는다']:
                    self.assertIn(required, body)

    def test_relative_links_in_changed_policy_documents_exist(self):
        for relative in ['AGENTS.md', '.claude/commands/retro.md',
                         '.claude/commands/archive.md', 'references/model-routing.md',
                         'references/workflow-policy.md',
                         'references/field-status-and-closeout.md']:
            path = ROOT / relative
            for link in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' in link or link.startswith('#'):
                    continue
                with self.subTest(file=relative, link=link):
                    self.assertTrue((path.parent / link.split('#')[0]).exists())


if __name__ == '__main__':
    unittest.main()
