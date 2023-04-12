from backend.mms_app_backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)
post = client.post
get = client.get


def test_signup():
    response = get('/signup')
    assert response.status_code == 405
    assert response.json() == {"detail":"Method Not Allowed"}
