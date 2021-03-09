import requests
import json


def test_delete_vacation():
    url = "http://localhost:8080/user/delete/1"
    payload = {"dateRange": "2021-03-11 tot 2021-03-14"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reservation"] is None
    print(response.text)


test_delete_vacation()
