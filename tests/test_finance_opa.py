from sovereign_platform.finance_service import execute_finance_task

def test_finance_opa_valid():
    bir = {
        'action': 'analyze',
        'target': 'PTT',
        'has_disclaimer': True,
        'risk_level': 'LOW'
    }
    result = execute_finance_task(bir)
    assert result['status'] == 'SUCCESS'

def test_finance_opa_missing_disclaimer():
    bir = {
        'action': 'analyze',
        'target': 'PTT',
        'has_disclaimer': False, # ผิดกฎ!
        'risk_level': 'LOW'
    }
    result = execute_finance_task(bir)
    assert result['status'] == 'REJECTED'
    assert 'Missing mandatory disclaimer' in result['details']

def test_finance_opa_critical_risk():
    bir = {
        'action': 'analyze',
        'target': 'PTT',
        'has_disclaimer': True,
        'risk_level': 'CRITICAL' # ผิดกฎ!
    }
    result = execute_finance_task(bir)
    assert result['status'] == 'REJECTED'
    assert 'Risk level too high' in result['details']