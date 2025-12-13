import pytest
from TestRestAPI.TestRestAPI import app, ENDPOINT


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# Extracted a function for test case parameterization
def get_payload_test_cases():
    return [
        ({"username": "test", "password": "pass123"}, 200),  # Valid case
        ({"password": "pass123"}, 400),  # Missing username
        ({"username": "test"}, 400),  # Missing password
        ({}, 400),  # Empty payload
    ]


@pytest.mark.parametrize("payload,expected_status", get_payload_test_cases())
def test_get_api_key_variations(client, payload, expected_status):
    response = client.post(ENDPOINT, json=payload)
    assert response.status_code == expected_status


def test_non_post_method_not_allowed(client):
    response = client.get(ENDPOINT)
    assert response.status_code == 405
