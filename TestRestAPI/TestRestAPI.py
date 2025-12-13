import string

from flask import Flask, request as flask_request, jsonify as flask_jsonify
import random
app = Flask(__name__)
GENERATED_API_KEY_LENGTH = 16
ENDPOINT = '/get_api_key'


def build_key():
    """
    Generates a fake API key.

    :return: The generated fake API key.
    """
    fake_api_key = str(random.randint(1234567890, 9999999999))
    while len(fake_api_key) < GENERATED_API_KEY_LENGTH:
        letter_part = random.choice(string.ascii_lowercase)
        fake_api_key += letter_part
    return fake_api_key


def validate_credentials(data):
    # Extract username and password from the request
    username = data.get('username')
    password = data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return flask_jsonify({'error': 'Username and password required'}), 400
    return None


# noinspection GrazieInspection
@app.route(ENDPOINT, methods=['POST'])
def get_api_key():
    """
    The `get_api_key` function is a route handler function that handles the HTTP POST request to the endpoint '/get_api_key'.
    It accepts username and password from the request and returns a response containing a fake API key.

    :param request: The Flask request object.
    :return: A response containing the fake API key if username and password are provided,
    otherwise an error message is returned with HTTP status code 400.

    Example usage:

        # Assuming Flask is properly configured and initialized
        # Create a POST request to '/get_api_key' with JSON body containing username and password
        # Retrieve the response
        response = client.post('/get_api_key', json={'username': 'test', 'password': 'pass123'})

        # Access the response data
        data = response.get_json()
        api_key = data.get('api_key')
        print(api_key)

        Output: '1234567890abcdef'
    """
    data = flask_request.get_json()
    validation_error = validate_credentials(data)

    if validation_error:
        return validation_error

    # For the purpose of this mock, we accept any username/password and return a fake API key
    # fake_api_key = '1234567890abcdef'
    fake_api_key = build_key()

    return flask_jsonify({'api_key': fake_api_key}), 200


@app.route('/test_api_key', methods=['POST'])
def test_api_key():
    """
    Validates an API key passed via request.

    Accepts the API key from (checked in this order):
    - "X-API-Key" header
    - "Authorization" header with "Bearer <token>"
    - JSON body field: {"api_key": "..."}

    Returns 200 with a success message if valid, otherwise 400 with an error.
    """
    # Try headers first
    api_key = request.headers.get('X-API-Key')

    if not api_key:
        auth_hdr = request.headers.get('Authorization', '')
        if auth_hdr.lower().startswith('bearer '):
            api_key = auth_hdr.split(' ', 1)[1].strip()

    # Fallback to JSON body
    if not api_key:
        body = request.get_json(silent=True) or {}
        api_key = body.get('api_key')

    if not api_key:
        return jsonify({'error': 'API key required'}), 400

    if not validate_api_key(api_key):
        return jsonify({'error': 'Invalid API key format'}), 400

    return jsonify({'message': 'API key is valid'}), 200


if __name__ == '__main__':
    app.run(debug=True)
