"""Static instruction-scope checks; not live LLM behavior tests."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PrepareScopeContracts(unittest.TestCase):
    def test_late_change_notes_do_not_require_a_new_json_output(self):
        body = (ROOT / '.claude/commands/prepare.md').read_text()
        required = ['기존 `preparation.md` 또는 runbook', '결과 JSON이 이미 있고',
                    '변경이 승인된 경우에만', '새 schema를 강제하지 않는다']
        self.assertTrue(all(text in body for text in required),
                        'Late-change notes must use existing records and condition JSON writes on existence and approval')
        self.assertNotIn('바꾼 부분은 결과 JSON과 README에 검증 범위 밖으로 표시한다.', body)

    def test_model_judgment_products_keep_their_existing_evaluation_path(self):
        body = (ROOT / '.claude/commands/prepare.md').read_text()
        required = ['독립 계산으로 결정되는', '모델이 분류·텍스트 판정을 수행하는 제품',
                    '`/demo`의 독립 expected']
        self.assertTrue(all(text in body for text in required),
                        'Numeric-engine guidance must not forbid independently evaluated model judgments')
        self.assertNotIn('숫자·판정은 계산 엔진이 만들고 모델은 그 숫자로만 쓰게 한다.', body)

if __name__ == '__main__':
    unittest.main()
