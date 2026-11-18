"""Static prompt contracts, not proof of model compliance or product usability."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


class ApprovalAndIntegrationContracts(unittest.TestCase):
    def test_agents_uses_role_names_and_criteria_before_ui(self):
        body = read('AGENTS.md')
        self.assertIn('| `/demo criteria` |', body)
        self.assertIn('| `/demo verify` |', body)
        self.assertIn('설계 초안 → criteria 고정 → 승인된 실제 UI 구현', body)
        self.assertNotIn('pre-event 실행은 `/design` 뒤', body)

    def test_design_preserves_approved_baseline_and_marks_unapproved_delta(self):
        body = read('.claude/commands/design.md')
        self.assertIn('승인된 설계 원본을 보존', body)
        self.assertIn('구현 차이', body)
        self.assertIn('승인 대기', body)
        self.assertNotIn('문서와 구현이 다르면 구현을 기준으로 문서를 갱신한다.', body)

    def test_template_does_not_grant_publication_permission(self):
        body = read('references/workflow-policy.md')
        for required in ['## 게시 권한', '템플릿 사용은 게시 승인이 아니다',
                         '로컬 수정 / stage·commit / push', '대상 저장소·branch·경로',
                         '이미 확인한 승인', '현재 사용자의 명시적 금지']:
            self.assertIn(required, body)
        paths = [ROOT / 'AGENTS.md'] + list((ROOT / '.claude/commands').glob('*.md'))
        for path in paths:
            with self.subTest(path=path.name):
                self.assertNotIn('상시 승인', path.read_text(encoding='utf-8'))
                if '## 종료 게시 절차' in path.read_text(encoding='utf-8'):
                    self.assertIn('게시 권한', path.read_text(encoding='utf-8'))

    def test_readmes_and_registration_explain_permission_boundary(self):
        self.assertIn('게시 권한', read('README.md'))
        self.assertIn('publication permission', read('README.en.md'))
        self.assertIn('게시 권한', read('.claude/commands/init.md'))
        self.assertIn('게시 권한', read('.claude/commands/onboard.md'))
        self.assertIn('읽기 전용', read('.claude/commands/onboard.md'))

    def test_team_choice_is_not_automatically_shared_adoption(self):
        for path in ['references/team-participation.md', '.claude/commands/ideate.md']:
            body = read(path)
            for required in ['개인 검토안', '팀 채택', '모호할 때만', '전원 동의']:
                with self.subTest(path=path, phrase=required):
                    self.assertIn(required, body)
        self.assertIn('공유 `product`를 덮어쓰지 않는다', read('.claude/commands/ideate.md'))

    def test_confirmed_product_name_requires_team_adoption_in_naming_paragraph(self):
        body = read('.claude/commands/ideate.md')
        naming = next(p for p in body.split('\n\n')
                      if p.startswith('선택 확정과 함께 제품명을'))
        # The earlier general product boundary must also govern this write path.
        self.assertIn('확정명·임시 코드명 기록 모두 위 제품 결정의 적용 범위에 종속된다', naming)
        self.assertRegex(
            naming,
            r'개인 행사에서는 사용자 선택, 팀 행사에서는 팀 채택 전달로 확인된 제품명만 '
            r'`hackathon.yaml`의 `product.name`에 기록한다\.')
        self.assertNotIn('사용자가 결정하면 `hackathon.yaml`의 `product.name`에 기록한다', naming)

    def test_temporary_codename_delay_does_not_bypass_team_adoption(self):
        body = read('.claude/commands/ideate.md')
        naming = next(p for p in body.split('\n\n')
                      if p.startswith('선택 확정과 함께 제품명을'))
        # Inspect the delay branch itself, not boundary words elsewhere in the file.
        delay = next(s for s in naming.split('. ') if s.startswith('결정이 늦어지면'))
        self.assertIn('임시 코드명을 제안하되', delay)
        self.assertIn('같은 적용 범위에서 채택이 확인된 경우에만 `product.name`에 기록', delay)
        self.assertIn('팀 채택 미확인 이름은 기존 ideation/notes의 개인후보로 유지', naming)
        self.assertIn('공유 `product.name`에 기록하지 않는다', naming)
        # Clear team decisions remain sufficient; no new unanimity/reconfirmation gate.
        self.assertIn('적용 범위가 모호할 때만 확인', body)
        self.assertIn('명확한 팀 결정 전달을 반복 확인하거나 전원 동의를 요구하지 않는다', body)

    def test_retrospective_checks_keep_oracle_quarantine(self):
        body = read('references/workflow-policy.md')
        for required in ['## 사후 기준과 인계', '사전 독립 acceptance',
                         '선행 명세', '사후 기능 점검', '다른 모델',
                         'ORACLE INVALID', 'PASS로 되살리지 않는다']:
            self.assertIn(required, body)
        self.assertIn('사후 기준과 인계', read('.claude/commands/demo.md'))
        self.assertIn('사후 기준과 인계', read('references/model-routing.md'))
        self.assertIn('사후 기준과 인계', read('.claude/commands/preflight.md'))

    def test_integration_sample_is_conditional_and_handles_absence(self):
        body = read('references/delivery-handoffs.md')
        for required in ['외부 데이터나 분리 구현이 있을 때만', '실제 표본 하나',
                         'ID·좌표·단위·시각', '범위 밖·결측', 'API·DB·새 schema']:
            self.assertIn(required, body)
        self.assertIn('첫 통합 표본', read('templates/execution-plan.md'))

    def test_integration_traces_approved_scope_not_all_possible_features(self):
        body = read('references/delivery-handoffs.md')
        for required in ['핵심 연결', '명세 → contract case 또는 승인된 제외',
                         '송신·수신', '해당 제품이 약속한', '다음 행동']:
            self.assertIn(required, body)
        for path in ['.claude/commands/demo.md', '.claude/commands/preflight.md',
                     'templates/execution-plan.md']:
            with self.subTest(path=path):
                self.assertIn('핵심 연결', read(path))

    def test_optional_human_observation_is_not_automated_actor_or_gate(self):
        body = read('references/delivery-handoffs.md')
        for required in ['선택적 실제 사용 관찰', '수행자', '진행자 개입',
                         '자동화의 human', '필수 설문', '효과 일반화', '완료 gate']:
            self.assertIn(required, body)
        self.assertIn('선택적 실제 사용 관찰', read('.claude/commands/prepare.md'))

    def test_touched_guidance_links_resolve(self):
        paths = [ROOT / 'AGENTS.md', ROOT / 'README.md', ROOT / 'README.en.md']
        paths += list((ROOT / '.claude/commands').glob('*.md'))
        paths += [ROOT / 'references' / name for name in
                  ['workflow-policy.md', 'delivery-handoffs.md',
                   'team-participation.md', 'model-routing.md']]
        paths += [ROOT / 'templates/execution-plan.md']
        for path in paths:
            for url in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' in url or url.startswith('#'):
                    continue
                with self.subTest(path=path.name, link=url):
                    self.assertTrue((path.parent / url.split('#')[0]).is_file())


if __name__ == '__main__':
    unittest.main()
