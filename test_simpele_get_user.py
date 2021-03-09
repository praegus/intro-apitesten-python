import json
import requests


def test_simpele_get_user():
    url = "http://localhost:8080/user/1"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["lastname"] == "MacDonald"
    print(response.text)


test_simpele_get_user()
