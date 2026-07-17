from utils.api_client import get


def test_invalid_post():
    response = get("/9999")

    assert response.status_code == 404