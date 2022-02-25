from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_root():
    response = client.get("theapp/")
    assert response.status_code == 200
