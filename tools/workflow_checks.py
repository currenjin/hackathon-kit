"""Read-only workflow consistency checks. Never certifies product acceptance."""
import argparse
import json
import math
from pathlib import Path

import yaml


def _positive(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value) and value > 0


def _valid_shape(data, contract=None):
    if not isinstance(data, dict):
        return False
    if any(key in data and not isinstance(data[key], dict)
           for key in ['event', 'presentation', 'submission', 'closeout', 'product']):
        return False
    if data.get('demo_contract') is not None and not isinstance(data['demo_contract'], str):
        return False
    p = data.get('presentation', {})
    if any(p.get(key) is not None and not isinstance(p[key], str)
           for key in ['source', 'timing_status']):
        return False
    return contract is None or isinstance(contract, dict)


def presentation_budget(data):
    """Resolve a preparation budget without changing official or historical data."""
    if not _valid_shape(data):
        raise ValueError('invalid workflow structure')
    official = data.get('event', {}).get('pitch_minutes')
    p = data.get('presentation', {})
    if official is not None:
        if not _positive(official):
            raise ValueError('invalid official pitch_minutes')
        return official * 60
    if p.get('timing_status') in {'user-confirmed', 'user_confirmed_range'}:
        value = p.get('effective_seconds')
        if not p.get('source') or p.get('source') == 'user-default' or not _positive(value):
            raise ValueError('user-confirmed budget requires source and positive seconds')
        bounds = p.get('allowed_range_seconds')
        if bounds is not None:
            if not isinstance(bounds, list) or len(bounds) != 2 or not all(_positive(v) for v in bounds):
                raise ValueError('invalid user-confirmed range')
            if not bounds[0] <= value <= bounds[1]:
                raise ValueError('target outside user-confirmed range')
        return value
    if 'effective_seconds' in p:
        if not _positive(p['effective_seconds']):
            raise ValueError('invalid recorded budget')
        return p['effective_seconds']  # Preserve legacy value; provenance is diagnosed separately.
    return 60


def aggregate_checks(checks):
    """Aggregate required subchecks only; caller must supply actual observations."""
    values = set(checks)
    allowed = {'PASS', 'PRODUCT FAIL', 'MODEL ERROR', 'INFRA ERROR', 'ORACLE INVALID', 'UNVERIFIED', 'NOT_RUN'}
    if values - allowed:
        raise ValueError('unknown verdict')
    for verdict in ['ORACLE INVALID', 'PRODUCT FAIL', 'MODEL ERROR', 'INFRA ERROR']:
        if verdict in values:
            return verdict
    return 'PASS' if values == {'PASS'} else 'UNVERIFIED'


def check_state(data, scope='submission', contract=None):
    """Return diagnostic codes, not permission, product PASS or automatic edits."""
    if scope not in {'submission', 'presentation', 'archive'}:
        raise ValueError('unknown scope')
    if not _valid_shape(data, contract):
        return ['WORKFLOW_STRUCTURE_INVALID']
    issues = []
    p = data.get('presentation', {})
    official = data.get('event', {}).get('pitch_minutes')
    source_known = bool(p.get('source')) and p.get('source') not in {'user-default', 'unknown', 'unverified'}
    if official is not None and not (source_known and p.get('timing_status') == 'official'):
        issues.append('PRESENTATION_SOURCE_UNVERIFIED')
    elif official is None and p.get('effective_seconds', 60) != 60 and not (
            source_known and p.get('timing_status') in {'user-confirmed', 'user_confirmed_range'}):
        issues.append('PRESENTATION_SOURCE_UNVERIFIED')
    submission = data.get('submission', {})
    closeout = data.get('closeout', {})
    try:
        seconds = presentation_budget(data)
        if data.get('event', {}).get('pitch_minutes') is not None and p.get('effective_seconds', seconds) != seconds:
            issues.append('PRESENTATION_BUDGET_STALE')
    except ValueError:
        issues.append('PRESENTATION_BUDGET_INVALID')
    if scope == 'presentation':
        if p.get('status') == 'presented_user_reported':
            issues.append('HISTORICAL_READINESS_UNVERIFIED')
        elif p.get('status') != 'ready':
            issues.append('PRESENTATION_NOT_READY')
    if scope == 'submission':
        if submission.get('status') == 'submitted_user_confirmed':
            issues.append('RECEIPT_NOT_READ_BACK')
        elif submission.get('status') != 'submitted':
            issues.append('SUBMISSION_UNCONFIRMED')
    if submission.get('status') == 'draft' and submission.get('user_reported_submitted'):
        issues.append('SUBMISSION_REPORT_STATE_CONFLICT')
    if scope == 'archive':
        service = closeout.get('service_status')
        if not service:
            issues.append('CURRENT_SERVICE_STATE_UNRECORDED')
        elif service == 'ended' and str(data.get('product', {}).get('implementation_status', '')).lower().startswith('deployed'):
            issues.append('CURRENT_SERVICE_STATE_CONFLICT')
    if contract:
        product = data.get('product', {}).get('name')
        expected_product = contract.get('product')
        if isinstance(expected_product, dict):
            expected_product = expected_product.get('name')
        if product and isinstance(expected_product, str) and expected_product != product:
            issues.append('PRODUCT_CONTRACT_MISMATCH')
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workspace', type=Path)
    parser.add_argument('--scope', choices=['submission', 'presentation', 'archive'], default='submission')
    args = parser.parse_args()
    root = args.workspace.resolve()
    issues = []
    try:
        data = yaml.safe_load((root / 'hackathon.yaml').read_text())
        if not _valid_shape(data):
            issues = ['WORKFLOW_STRUCTURE_INVALID']
        else:
            contract = None
            reference = data.get('demo_contract')
            if reference:
                path = (root / reference).resolve()
                if not path.is_relative_to(root):
                    issues = ['CONTRACT_OUTSIDE_WORKSPACE']
                elif path.suffix == '.json':
                    contract = json.loads(path.read_text())
            if not issues:
                issues = check_state(data, scope=args.scope, contract=contract)
    except (OSError, yaml.YAMLError, ValueError):
        issues = ['WORKFLOW_INPUT_UNREADABLE']
    print(json.dumps({'scope': args.scope, 'diagnostics': issues,
                      'read_only': True, 'product_acceptance_checked': False}, ensure_ascii=False))
    return 1 if issues else 0


if __name__ == '__main__':
    raise SystemExit(main())
