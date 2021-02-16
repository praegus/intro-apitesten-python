import requests
import json


def test_simpele_post():
    url = "http://localhost:8080/user/reserve/1"
    payload = {"dateRange": "2021-02-11 tot 2021-02-14"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


test_simpele_post()
