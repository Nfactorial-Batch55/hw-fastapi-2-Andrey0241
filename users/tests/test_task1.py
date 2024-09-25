import requests


def test_task1_users():
    response = requests.get("http://localhost:8000/users")
    assert "Robin Monroe" in response.text
    assert "alexandriajohnson" in response.text
    assert 'href="/users/87' in response.text


def test_task1_user1():
    response = requests.get("http://localhost:8000/users/90")
    assert "Francisco Osborne" in response.text
    assert "catherinegreen@hotmail.com" in response.text
    assert "wward" in response.text


def test_task1_user2():
    response = requests.get("http://localhost:8000/users/17")
    assert "Andrew Thomas" in response.text
    assert "seanhunter" in response.text
    assert "bmontoya@gmail.com" in response.text


def test_task1_user_not_found():
    response = requests.get("http://localhost:8000/users/789")
    assert response.text == "Not found"
    assert response.status_code == 404
