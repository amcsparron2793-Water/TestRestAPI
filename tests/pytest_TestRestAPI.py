import pytest
from TestRestAPI.TestRestAPI import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize("payload,expected_status", [
    ({"username": "test", "password": "pass123"}, 200),  # Valid case
    ({"password": "pass123"}, 400),  # Missing username
    ({"username": "test"}, 400),  # Missing password
    ({}, 400),  # Empty payload
])
def test_get_api_key_variations(client, payload, expected_status):
    response = client.post("/get_api_key", json=payload)
    assert response.status_code == expected_status
