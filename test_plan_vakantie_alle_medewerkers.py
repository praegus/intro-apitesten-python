import requests
import json

content_type = 'application/json'


def test_maak_reservering_voor_paul():
    url = "http://localhost:8080/user/reserve/1"
    payload = {"dateRange": "2021-03-11 tot 2021-03-14"}
    headers = {
        'Content-Type': content_type
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


def test_maak_reservering_voor_anna():
    url = "http://localhost:8080/user/reserve/2"
    payload = {"dateRange": "2021-04-11 tot 2021-04-14"}
    headers = {
        'Content-Type': content_type
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


def test_maak_reservering_voor_luke():
    url = "http://localhost:8080/user/reserve/3"
    payload = {"dateRange": "2021-05-11 tot 2021-05-14"}
    headers = {
        'Content-Type': content_type
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


def test_maak_reservering_voor_kim():
    url = "http://localhost:8080/user/reserve/4"
    payload = {"dateRange": "2021-06-11 tot 2021-06-14"}
    headers = {
        'Content-Type': content_type
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


def test_maak_reservering_voor_dan():
    url = "http://localhost:8080/user/reserve/5"
    payload = {"dateRange": "2021-07-11 tot 2021-07-14"}
    headers = {
        'Content-Type': content_type
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


def test_maak_reservering_voor_anthony():
    url = "http://localhost:8080/user/reserve/6"
    payload = {"dateRange": "2021-08-11 tot 2021-08-14"}
    headers = {
        'Content-Type': content_type
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


def test_maak_reservering_voor_jake():
    url = "http://localhost:8080/user/reserve/7"
    payload = {"dateRange": "2021-09-11 tot 2021-09-14"}
    headers = {
        'Content-Type': content_type
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


def test_maak_reservering_voor_joanne():
    url = "http://localhost:8080/user/reserve/8"
    payload = {"dateRange": "2021-10-11 tot 2021-10-14"}
    headers = {
        'Content-Type': content_type
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


test_maak_reservering_voor_paul()
test_maak_reservering_voor_anna()
test_maak_reservering_voor_luke()
test_maak_reservering_voor_kim()
test_maak_reservering_voor_dan()
test_maak_reservering_voor_anthony()
test_maak_reservering_voor_jake()
test_maak_reservering_voor_joanne()
