"""Synthetic policy checks, not deployed UI or model acceptance tests."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / 'tools/workflow_checks.py'


class WorkflowBehavior(unittest.TestCase):
    def setUp(self):
        self.assertTrue(MODULE_PATH.exists(), 'read-only workflow checker is missing')
        spec = importlib.util.spec_from_file_location('workflow_checks', MODULE_PATH)
        assert spec is not None and spec.loader is not None
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def test_user_range_preserved_without_official_time(self):
        data = {'event': {'pitch_minutes': None}, 'presentation': {
            'effective_seconds': 210, 'timing_status': 'user_confirmed_range',
            'source': 'user-message', 'allowed_range_seconds': [180, 240]}}
        before = copy.deepcopy(data)
        self.assertEqual(self.module.presentation_budget(data), 210)
        self.assertEqual(data, before)

    def test_target_outside_user_range_rejected(self):
        with self.assertRaises(ValueError):
            self.module.presentation_budget({'presentation': {'effective_seconds': 250,
                'timing_status': 'user_confirmed_range', 'source': 'user-message',
                'allowed_range_seconds': [180, 240]}})

    def test_user_time_requires_source(self):
        with self.assertRaises(ValueError):
            self.module.presentation_budget({'presentation': {'effective_seconds': 210,
                'timing_status': 'user_confirmed_range', 'allowed_range_seconds': [180, 240]}})

    def test_official_time_takes_precedence(self):
        self.assertEqual(self.module.presentation_budget({'event': {'pitch_minutes': 2},
            'presentation': {'effective_seconds': 210}}), 120)

    def test_invalid_official_time_not_hidden_by_default(self):
        for value in [0, -1, 'three', True]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.module.presentation_budget({'event': {'pitch_minutes': value}})

    def test_legacy_record_uses_default_without_mutation(self):
        data = {}
        self.assertEqual(self.module.presentation_budget(data), 60)
        self.assertEqual(data, {})

    def test_hidden_required_ui_prevents_pass(self):
        self.assertEqual(self.module.aggregate_checks(['PASS', 'PRODUCT FAIL']), 'PRODUCT FAIL')

    def test_missing_observation_not_promoted_to_pass(self):
        for values in [[], ['PASS', 'UNVERIFIED'], ['PASS', 'NOT_RUN']]:
            self.assertEqual(self.module.aggregate_checks(values), 'UNVERIFIED')

    def test_failed_case_not_softened_by_incomplete_observation(self):
        self.assertEqual(self.module.aggregate_checks(['PRODUCT FAIL', 'NOT_RUN']), 'PRODUCT FAIL')

    def test_all_required_checks_pass(self):
        self.assertEqual(self.module.aggregate_checks(['PASS', 'PASS']), 'PASS')

    def test_unknown_verdict_rejected(self):
        with self.assertRaises(ValueError):
            self.module.aggregate_checks(['looks-good'])

    def test_candidate_can_submit_without_finalist_pitch_ready(self):
        data = {'submission': {'status': 'submitted_user_confirmed'},
                'presentation': {'selection_status': 'pending', 'status': 'pending'}}
        self.assertNotIn('PRESENTATION_NOT_READY', self.module.check_state(data, scope='submission'))
        self.assertNotIn('SUBMISSION_UNCONFIRMED', self.module.check_state(data, scope='submission'))

    def test_presentation_scope_still_requires_ready(self):
        self.assertIn('PRESENTATION_NOT_READY', self.module.check_state(
            {'presentation': {'status': 'dirty'}}, scope='presentation'))

    def test_reported_presentation_is_not_retroactively_marked_unready(self):
        issues = self.module.check_state({'presentation': {'status': 'presented_user_reported'}}, scope='presentation')
        self.assertNotIn('PRESENTATION_NOT_READY', issues)
        self.assertIn('HISTORICAL_READINESS_UNVERIFIED', issues)

    def test_user_submission_is_not_direct_receipt_readback(self):
        self.assertIn('RECEIPT_NOT_READ_BACK', self.module.check_state(
            {'submission': {'status': 'submitted_user_confirmed'}}, scope='submission'))

    def test_reported_submission_not_reset_to_draft(self):
        data = {'submission': {'status': 'draft', 'user_reported_submitted': True}}
        self.assertIn('SUBMISSION_REPORT_STATE_CONFLICT', self.module.check_state(data))

    def test_ended_service_cannot_remain_currently_deployed(self):
        data = {'product': {'implementation_status': 'deployed'},
                'closeout': {'service_status': 'ended'}}
        self.assertIn('CURRENT_SERVICE_STATE_CONFLICT', self.module.check_state(data, scope='archive'))

    def test_archive_requires_explicit_current_state_not_http200_inference(self):
        self.assertIn('CURRENT_SERVICE_STATE_UNRECORDED', self.module.check_state({}, scope='archive'))

    def test_contract_of_other_product_is_detected(self):
        data = {'product': {'name': 'Example App'}}
        self.assertIn('PRODUCT_CONTRACT_MISMATCH', self.module.check_state(data, contract={'product': 'Selfie Building'}))

    def test_scope_checker_does_not_migrate_legacy_fields(self):
        data = {'product': {'name': 'Example App'}}
        before = copy.deepcopy(data)
        self.module.check_state(data)
        self.assertEqual(data, before)

    def test_official_time_without_source_is_flagged(self):
        issues = self.module.check_state({'event': {'pitch_minutes': 3}})
        self.assertIn('PRESENTATION_SOURCE_UNVERIFIED', issues)

    def test_unattributed_legacy_budget_is_preserved_and_flagged(self):
        data = {'presentation': {'effective_seconds': 210}}
        self.assertEqual(self.module.presentation_budget(data), 210)
        self.assertIn('PRESENTATION_SOURCE_UNVERIFIED', self.module.check_state(data))
        self.assertEqual(data['presentation']['effective_seconds'], 210)

    def test_invalid_mapping_returns_diagnostic(self):
        for data in [None, [], {'presentation': None}, {'event': 'bad'}, {'submission': []}]:
            with self.subTest(data=data):
                self.assertEqual(self.module.check_state(data), ['WORKFLOW_STRUCTURE_INVALID'])

    def test_cli_invalid_yaml_shapes_return_json(self):
        for source in ['null\n', '[]\n', 'presentation: null\n', 'demo_contract: 12\n', 'demo_contract: []\n']:
            with self.subTest(source=source), tempfile.TemporaryDirectory() as temp:
                (Path(temp) / 'hackathon.yaml').write_text(source)
                result = subprocess.run([sys.executable, '-B', str(MODULE_PATH), temp],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 1)
                self.assertIn('WORKFLOW_STRUCTURE_INVALID', json.loads(result.stdout)['diagnostics'])
                self.assertNotIn('Traceback', result.stderr)

    def test_cli_diagnostics_are_read_only(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'hackathon.yaml'
            source = 'product:\n  implementation_status: deployed\ncloseout:\n  service_status: ended\n'
            path.write_text(source)
            result = subprocess.run([sys.executable, '-B', str(MODULE_PATH), temp,
                                     '--scope', 'archive'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('CURRENT_SERVICE_STATE_CONFLICT', json.loads(result.stdout)['diagnostics'])
            self.assertEqual(path.read_text(), source)
            self.assertEqual([p.name for p in Path(temp).iterdir()], ['hackathon.yaml'])

    def test_cli_rejects_contract_outside_workspace(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workspace = root / 'event'
            workspace.mkdir()
            (root / 'outside.json').write_text('{"product": "other"}')
            (workspace / 'hackathon.yaml').write_text('demo_contract: ../outside.json\n')
            result = subprocess.run([sys.executable, '-B', str(MODULE_PATH), str(workspace)],
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('CONTRACT_OUTSIDE_WORKSPACE', json.loads(result.stdout)['diagnostics'])
            self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
