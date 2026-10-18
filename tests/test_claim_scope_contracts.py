"""Static claim-scope guidance checks, not semantic verification or model execution."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ClaimScopeContracts(unittest.TestCase):
    def test_humanize_checks_scope_after_style_edits(self):
        body = (ROOT / '.claude/commands/humanize.md').read_text()
        self.assertIn('문체 수정 뒤 사실 범위 재검수', body)
        self.assertIn('../../references/claim-scope-check.md', body)

    def test_present_checks_scope_before_render_and_publication(self):
        body = (ROOT / '.claude/commands/present.md').read_text()
        self.assertIn('문체 수정 뒤 사실 범위 재검수', body)
        self.assertIn('../../references/claim-scope-check.md', body)
        self.assertLess(body.index('문체 수정 뒤 사실 범위 재검수'), body.index('## 등록과 확인'))

    def test_shared_check_preserves_evidence_boundaries(self):
        body = (ROOT / 'references/claim-scope-check.md').read_text()
        for token in ['수치·조건·한계', '모든/항상/절대', '고정된 expected',
                      '구조 검사', '의미 정확성', 'SDK', '다른 제품', '미검증']:
            self.assertIn(token, body)

    def test_scope_check_does_not_authorize_new_facts_or_release(self):
        body = (ROOT / 'references/claim-scope-check.md').read_text()
        for token in ['일괄 금지하지 않는다', '승인 없이 사실을 새로 쓰지 않는다',
                      '수치나 expected를 출력에 맞춰 바꾸지 않는다', '제품 PASS', '리허설']:
            self.assertIn(token, body)


if __name__ == '__main__':
    unittest.main()
