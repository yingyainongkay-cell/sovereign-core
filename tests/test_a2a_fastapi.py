from fastapi.testclient import TestClient
from sovereign_platform.a2a_gateway import app
client = TestClient(app)
def test_a2a_valid():
    payload = {'author_role': 'developer', 'verifier_role': 'auditor', 'evidence_refs': ['sha256:123'], 'ledger_hash': '0x7f8c9b123456'}
    response = client.post('/api/v1/a2a/handoff', json=payload)
    assert response.status_code == 200
