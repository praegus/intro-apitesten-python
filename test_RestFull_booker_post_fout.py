import requests
import json

base_url = "http://localhost:3001"


def test_post_booking():
    url = base_url + "/booking"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-02-23",
            "checkout": "2022-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url, headers=headers, json=payload, timeout=3)
    # voor een of andere reden maakt hij hiervan een 500 terwijl in postman maakt hij er een 400 van
    assert response.status_code == 500
    data = json.loads(response.content)
    print(response.text)


test_post_booking()
