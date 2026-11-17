from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'OK'

def test_api_valid_command():
    payload = {
        'text': 'สั่ง: วิเคราะห์ PTT ถ้า RSI < 30 ให้ เตือน',
        'has_disclaimer': True,
        'risk_level': 'LOW'
    }
    response = client.post('/api/v1/execute', json=payload)
    assert response.status_code == 200
    assert response.json()['status'] == 'SUCCESS'

def test_api_blocked_by_opa():
    payload = {
        'text': 'สั่ง: วิเคราะห์ PTT ถ้า RSI < 30 ให้ เตือน',
        'has_disclaimer': False, # ลืม Disclaimer
        'risk_level': 'LOW'
    }
    response = client.post('/api/v1/execute', json=payload)
    assert response.status_code == 200
    assert response.json()['status'] == 'REJECTED'