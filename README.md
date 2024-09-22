# TestRestAPI

This project is a simple Flask application that generates and returns a fake API key based on the provided username and password.

## Overview

The core functionality of this application is to receive a `POST` request at the endpoint `/get_api_key`, process the input data (username and password), and respond with a fake API key.

## Setup

### Prerequisites

- Python 3.12.3
- Flask
- Jinja2
- Werkzeug
- click
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install Flask Jinja2 Werkzeug click
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Send a `POST` request to `http://127.0.0.1:5000/get_api_key` with JSON payload containing the username and password:

   Example using `curl`:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username": "test", "password": "pass123"}' http://127.0.0.1:5000/get_api_key
    ```

   Example using Python `requests` library:
    ```python
    import requests

    url = "http://127.0.0.1:5000/get_api_key"
    payload = {"username": "test", "password": "pass123"}
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("API Key:", data.get("api_key"))
    else:
        print("Error:", response.status_code, response.json())
    ```

## Example Response

- **Request**:
    ```json
    {
        "username": "test",
        "password": "pass123"
    }
    ```

- **Response**:
    ```json
    {
        "api_key": "1234567890abcdef"
    }
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.