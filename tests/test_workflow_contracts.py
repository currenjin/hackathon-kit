"""Static documentation contracts, NOT a model-run or event compliance test.

Run: python -B -m unittest discover -s tests -v
PyYAML is needed to validate the actual template and frontmatter.
"""
from pathlib import Path
import re
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = ROOT / '.claude/commands'


def text(name):
    return (COMMANDS / (name + '.md')).read_text()


class WorkflowContracts(unittest.TestCase):
    def test_all_command_frontmatter_and_policy_links(self):
        for path in COMMANDS.glob('*.md'):
            with self.subTest(command=path.name):
                body = path.read_text()
                self.assertTrue(body.startswith('---\n'))
                self.assertIn('description', yaml.safe_load(body.split('---', 2)[1]))
                self.assertIn('references/workflow-policy.md', body)
                self.assertIn('인용문', body)

    def test_document_links(self):
        files = list(COMMANDS.glob('*.md')) + [
            ROOT / 'README.md', ROOT / 'references/workflow-policy.md',
            ROOT / 'references/presentation-reference-guide.md',
            ROOT / 'references/pre-event-readiness.md',
            ROOT / '.claude/rules/design.md', ROOT / '.claude/rules/language.md',
            ROOT / '.claude/rules/writing/common.md',
        ]
        for path in files:
            for url in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in url or url.startswith('#'):
                    continue
                with self.subTest(file=path.name, link=url):
                    self.assertTrue((path.parent / url.split('#')[0]).exists())

    def test_readiness_reference_is_reachable_from_commands(self):
        for name in ['ideate', 'design', 'prepare', 'preflight']:
            with self.subTest(command=name):
                self.assertIn('references/pre-event-readiness.md', text(name))
        self.assertTrue((ROOT / 'references/pre-event-readiness.md').is_file())

    def test_readiness_has_three_product_gates_not_starter_only(self):
        body = (ROOT / 'references/workflow-policy.md').read_text()
        for required in ['제품 명세', '화면·상태 설계', '현장 실행 계획',
                         '스타터 준비', '사전 준비 미완료']:
            self.assertIn(required, body)

    def test_design_reviews_no_code_flow_without_claiming_ui_implementation(self):
        for required in ['사전설계 검토완료', '제품 UI 미구현',
                         '사용자 검토', '고정/가변', '상태 전이', '누락·모순']:
            self.assertIn(required, text('design'))

    def test_prepare_gates_product_work_before_packaging(self):
        body = text('prepare')
        for required in ['제품 명세', '화면·상태 설계', '현장 실행 계획',
                         '스타터 준비', '사전 준비 미완료', '독립 성공/실패 기준']:
            self.assertIn(required, body)

    def test_preflight_reports_plan_environment_and_live_readiness_separately(self):
        for required in ['제품 계획 준비', '실행환경 준비', '현장 확인 대기',
                         '핵심 결정', '사전 준비 미완료', '실제 제품 검증']:
            self.assertIn(required, text('preflight'))

    def test_readiness_criteria_keep_timing_and_permission_branches(self):
        body = (ROOT / 'references/workflow-policy.md').read_text()
        for required in ['/design(허용된 사전설계 검토)',
                         '공식 제한으로 준비 범위만 점검', '현장 확인 대기',
                         '금지된 코드·prompt·fixture']:
            self.assertIn(required, body)

    def test_policy_template_is_safe_by_default(self):
        policy = yaml.safe_load((ROOT / 'templates/hackathon.yaml').read_text())['build_policy']
        self.assertEqual(policy['mode'], 'restricted-preparation')
        self.assertEqual(policy['source'], '')
        self.assertIsNone(policy['starts_at'])
        self.assertIsNone(policy['ends_at'])
        self.assertEqual(policy['code_reuse'], 'unknown')
        self.assertEqual(set(policy['pre_event']), set('planning design prompt data criteria code deck pitch submission'.split()))
        self.assertTrue(all(v == 'unknown' for v in policy['pre_event'].values()))

    def test_three_documented_branches(self):
        body = (ROOT / 'references/workflow-policy.md').read_text()
        for mode in ['prebuild-permitted', 'on-site-build-only', 'restricted-preparation']:
            self.assertIn('### ' + mode, body)
        self.assertIn('preparation readiness', body)
        self.assertIn('product readiness', body)
        self.assertIn('미확인은 허용이 아니다', body)

    def test_replan_executes_init_and_ideate_not_only_advises(self):
        body = text('replan')
        for required in ['init 재확인을 실제 수행', 'ideate 전체 재평가',
                         '안내만 하고 종료하지 않는다', '명시적 예외',
                         '사용자 결정', '기존 아이디어 유지 / 수정 / 새 후보',
                         '코드 재사용 자격', '부분완료', 'init.md', 'ideate.md']:
            self.assertIn(required, body)
        self.assertIn('그 밖의 command 자동 실행은 승인하지 않는다', body)

    def test_init_refresh_preserves_identity_and_history(self):
        for required in ['빈칸만 채우는 규칙의 예외', 'URL·날짜', '이전값', '출처', 'workspace를 유지']:
            self.assertIn(required, text('init'))

    def test_demo_roles_and_legacy_aliases(self):
        body = text('demo')
        for required in ['criteria', 'verify', 'pre-event` → `criteria',
                         'on-site` → `verify', '독립', 'ORACLE INVALID', '공식 제작 시작 이후']:
            self.assertIn(required, body)
        self.assertNotIn('모드는 pre-event 또는 on-site', body)
        self.assertNotIn('pre-event에 scenario별', body)

    def test_prepare_can_build_on_site_without_pre_event_contract(self):
        for required in ['행사 전에 고정한 contract를 요구하지 않는다',
                         '공식 시작 이후 종료 전', '/demo criteria',
                         '출품용 구현 대기', '독립', '복구']:
            self.assertIn(required, text('prepare'))

    def test_adapt_initial_environment_exception_is_not_product_success(self):
        for required in ['환경설정 전용', '제품 미구현', 'E2E 미실시',
                         '제품 연결 모드', '현장 신규 구현 금지가 아니다']:
            self.assertIn(required, text('adapt'))

    def test_preflight_does_not_require_forbidden_prebuild(self):
        for required in ['preparation readiness', 'product readiness',
                         '필수 입력이 아니다', 'unknown은 RISK', 'N/A는 제품 PASS가 아니다']:
            self.assertIn(required, text('preflight'))

    def test_deliverables_and_auxiliary_commands_respect_policy(self):
        for name in ['deck', 'pitch', 'submit', 'decide', 'humanize', 'retro', 'archive']:
            with self.subTest(command=name):
                self.assertIn('workflow-policy.md', text(name))
        for name in ['deck', 'pitch', 'submit']:
            self.assertIn('build_policy', text(name))

    def test_historical_facts_and_active_version_are_preserved(self):
        body = text('replan')
        for required in ['active_version: null', 'superseded_versions',
                         '이미 실제 제출한 사실', '모든 단계를 일괄 초기화하지 않는다',
                         'commit 시각을 바꿔']:
            self.assertIn(required, body)


if __name__ == '__main__':
    unittest.main()
