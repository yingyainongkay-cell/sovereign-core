from sovereign_platform.orchestrator import SovereignOrchestrator

def test_e2e_happy_path():
    orchestrator = SovereignOrchestrator()
    # ภาษาไทยถูกต้อง + มี Disclaimer + ความเสี่ยงต่ำ -> ต้องผ่าน
    result = orchestrator.process_thai_command(
        'สั่ง: วิเคราะห์ PTT ถ้า RSI < 30 ให้ เตือน', 
        has_disclaimer=True, 
        risk_level='LOW'
    )
    assert result['status'] == 'SUCCESS'
    assert result['step'] == 'FINANCE_OPA_GATE'

def test_e2e_fail_on_grammar():
    orchestrator = SovereignOrchestrator()
    # ภาษาไทยผิด Grammar -> ต้องโดนบล็อกตั้งแต่ OCTL
    result = orchestrator.process_thai_command('ช่วยดูหุ้นให้หน่อย')
    assert result['status'] == 'REJECTED'
    assert result['step'] == 'OCTL_COMPILER'

def test_e2e_fail_on_policy():
    orchestrator = SovereignOrchestrator()
    # ภาษาไทยถูก แต่ลืม Disclaimer -> ต้องโดนบล็อกที่ OPA
    result = orchestrator.process_thai_command(
        'สั่ง: วิเคราะห์ PTT ถ้า RSI < 30 ให้ เตือน', 
        has_disclaimer=False, 
        risk_level='LOW'
    )
    assert result['status'] == 'REJECTED'
    assert result['step'] == 'FINANCE_OPA_GATE'
    assert 'Missing mandatory disclaimer' in result['data']['details']