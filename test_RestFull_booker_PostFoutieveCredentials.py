import requests
import json

base_url = "http://localhost:3001"


def test_post_user():
    url = base_url + "/auth"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "username": "admin",
        "password": "a"
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reason"] == "Bad credentials"
    print(response.text)


test_post_user()
