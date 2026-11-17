def evaluate_policy(bir: dict) -> dict:
    """
    จำลองการทำงานของ OPA (Open Policy Agent)
    ในระบบจริงจะเรียก OPA CLI หรือ API
    """
    # กฎ: ต้องมี Disclaimer และห้ามเสี่ยงระดับ CRITICAL
    if not bir.get('has_disclaimer', False):
        return {'allow': False, 'reason': 'FAIL-CLOSED: Missing mandatory disclaimer.'}
        
    if bir.get('risk_level') == 'CRITICAL':
        return {'allow': False, 'reason': 'FAIL-CLOSED: Risk level too high for automated execution.'}
        
    return {'allow': True, 'reason': 'Policy Check Passed.'}

def execute_finance_task(bir: dict) -> dict:
    policy_result = evaluate_policy(bir)
    if not policy_result['allow']:
        return {'status': 'REJECTED', 'details': policy_result['reason']}
        
    return {
        'status': 'SUCCESS',
        'action': bir.get('action'),
        'target': bir.get('target'),
        'message': 'Execution Authorized by OPA Gate.'
    }