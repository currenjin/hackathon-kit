"""Static handoff and example checks; not command/model execution or product E2E."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / 'references/delivery-handoffs.md'
CATALOG = ROOT / 'references/starter-references.md'
EXAMPLE = ROOT / 'examples/synthetic-handoff.md'
TEMPLATES = ['project-facts.md', 'execution-plan.md', 'judging-evidence.md']
COMMANDS = ['ideate', 'prepare', 'adapt', 'deck', 'pitch', 'submit', 'preflight']


class ReferenceAdoptionContracts(unittest.TestCase):
    def test_commands_discover_shared_handoff(self):
        for command in COMMANDS:
            with self.subTest(command=command):
                body = (ROOT / '.claude/commands' / (command + '.md')).read_text()
                self.assertIn('references/delivery-handoffs.md', body)

    def test_local_navigation_links_resolve(self):
        files = [GUIDE, CATALOG, EXAMPLE, ROOT / 'README.md']
        files.extend(ROOT / 'templates' / name for name in TEMPLATES)
        for path in files:
            for url in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' not in url and not url.startswith('#'):
                    with self.subTest(file=path.name, link=url):
                        self.assertTrue((path.parent / url.split('#')[0]).is_file())

    def test_handoffs_preserve_authority_and_existing_paths(self):
        body = GUIDE.read_text()
        for phrase in ['기존 경로', '자동 migration하지 않는다',
                       '원문과 실행 evidence', 'ORACLE INVALID', '자동 실행하지 않는다',
                       '금지·unknown', '별도 승인', '소급']:
            self.assertIn(phrase, body)

    def test_fact_sheet_is_traceable_and_versioned(self):
        body = (ROOT / 'templates/project-facts.md').read_text()
        for phrase in ['현재 build', 'claim', '출처', '검증 경로', '사용 가능 범위',
                       '미검증', '변경 영향', '일관성 검수', '제출 이력']:
            self.assertIn(phrase, body)

    def test_runbook_has_observable_checkpoints_not_fixed_hours(self):
        body = (ROOT / 'templates/execution-plan.md').read_text()
        for phrase in ['담당', '완료 증거', '확인 시점', '미달 시', '첫 E2E', '조기 배포',
                       '최초 호출', '비용', '독립 기준', '승인', 'readback']:
            self.assertIn(phrase, body)

    def test_rubric_does_not_replace_product_verdict(self):
        body = (ROOT / 'templates/judging-evidence.md').read_text()
        for phrase in ['공식 기준', '심사 점수', '미확인', '실행 evidence', 'local/mock',
                       '출품 자격', '제품 PASS']:
            self.assertIn(phrase, body)

    def test_examples_cannot_be_mistaken_for_real_evidence(self):
        body = EXAMPLE.read_text()
        self.assertIn('합성 예시', body)
        self.assertIn('실제 실행하지 않았다', body)
        self.assertIn('UNVERIFIED', body)
        self.assertNotIn('https://github.com/you/', body)
        self.assertIn('개인정보', body)

    def test_catalog_is_conditional_and_records_provenance(self):
        body = CATALOG.read_text()
        for phrase in ['udaysharmadev', 'IdkwhatImD0ing', 'CopilotKit', 'RachelBurman',
                       'sahat', '검토 commit', '라이선스', '실행 검증하지 않았다',
                       '62.5', '기본 스택', '공식 규칙']:
            self.assertIn(phrase, body)


if __name__ == '__main__':
    unittest.main()
