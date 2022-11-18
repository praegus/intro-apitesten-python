import requests
import json

base_url = "http://localhost:3001"


def test_post_booking():
    url = base_url + "/auth"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["token"]
    print(response.text)


test_post_booking()
