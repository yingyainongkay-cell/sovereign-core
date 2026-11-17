from sovereign_platform.octl_compiler import OCTLCompiler
from sovereign_platform.finance_service import execute_finance_task

class SovereignOrchestrator:
    def __init__(self):
        self.compiler = OCTLCompiler()
        
    def process_thai_command(self, raw_input: str, has_disclaimer: bool = False, risk_level: str = 'LOW') -> dict:
        # 1. Compile Thai -> BIR (ถ้าภาษาผิด จะ Fail-Closed ทันที)
        bir_result = self.compiler.compile(raw_input)
        if bir_result['status'] == 'FAIL_CLOSED':
            return {'status': 'REJECTED', 'step': 'OCTL_COMPILER', 'reason': bir_result['error']}
            
        # 2. แนบข้อมูล Context เพิ่มเติม (Disclaimer/Risk)
        bir = bir_result['bir']
        bir['has_disclaimer'] = has_disclaimer
        bir['risk_level'] = risk_level
        
        # 3. ส่งให้ Finance Service + OPA ตรวจสอบ
        finance_result = execute_finance_task(bir)
        
        return {
            'status': finance_result['status'],
            'step': 'FINANCE_OPA_GATE',
            'data': finance_result
        }