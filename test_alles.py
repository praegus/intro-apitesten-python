import json
import requests

# verzameling van alle testen om te draaien in 1 suite 


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

def test_get_naar_niet_bestaand_account():
    url = "http://localhost:8080/user/10"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 500
    data = json.loads(response.content)
    assert data["message"] == "No value present"
    print(response.text)


test_get_naar_niet_bestaand_account()

def test_maak_reservering():
    url = "http://localhost:8080/user/reserve/1"
    payload = {"dateRange": "2021-03-11 tot 2021-03-14"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["reserveringIsGoedgekeurd"] == True
    print(response.text)


test_maak_reservering()

def test_get_gebruiker_die_vakantie_heeft():
    url = "http://localhost:8080/user/1"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    data = json.loads(response.content)
    assert data["lastname"] == "MacDonald"
    assert data["reservation"]["startDate"] == "2021-03-11"
    print(response.text)


test_get_gebruiker_die_vakantie_heeft()

def test_maak_reservering_json_foutief():
    url = "http://localhost:8080/user/reserve/1"
    payload = {"dateRange": "2021-03-11 2021-03-14"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 500
    data = json.loads(response.content)
    assert data["error"] == "Internal Server Error"
    print(response.text)


test_maak_reservering_json_foutief()

def test_maak_dubbele_reservering():
    url = "http://localhost:8080/user/reserve/1"
    payload = {"dateRange": "2021-02-11 tot 2021-02-14"}
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload, timeout=3)
    assert response.status_code == 500
    data = json.loads(response.content)
    assert data["message"] == "User has an existing reservation"
    print(response.text)


test_maak_dubbele_reservering()

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



