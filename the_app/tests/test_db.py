from typing import TYPE_CHECKING

from fastapi.testclient import TestClient


if TYPE_CHECKING:
    from httpx import Response

from main import app


client = TestClient(app)


def test_root() -> None:
    EXPECTED_STATUS_CODE = 200
    response: Response = client.get("theapp/")
    assert response.status_code == EXPECTED_STATUS_CODE
