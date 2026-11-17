from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sovereign_platform.orchestrator import SovereignOrchestrator

app = FastAPI(title='Sovereign Core API', version='1.0.0')
orchestrator = SovereignOrchestrator()

class ThaiCommandRequest(BaseModel):
    text: str
    has_disclaimer: bool = False
    risk_level: str = 'LOW'

@app.post('/api/v1/execute')
def execute_command(req: ThaiCommandRequest):
    result = orchestrator.process_thai_command(
        raw_input=req.text,
        has_disclaimer=req.has_disclaimer,
        risk_level=req.risk_level
    )
    if result['status'] == 'REJECTED':
        # ในระบบจริงอาจจะ Return 200 พร้อมสถานะ REJECTED หรือ 403 ก็ได้
        # ที่นี่เราเลือก Return 200 เพื่อให้ Client เห็น Reason ชัดๆ
        return result
    return result

@app.get('/health')
def health_check():
    return {'status': 'OK', 'system': 'Sovereign Core'}