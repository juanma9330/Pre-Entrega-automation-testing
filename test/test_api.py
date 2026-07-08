import requests
import pytest_check as check
import pytest

headers = {
    "x-api-key": "pub_412f6b0d259a0458fcd8a7d4917dd5cf2477727ddc41295e65dc8f970347f030"
}

@pytest.mark.api
def test_login_valido():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    #assert response.status_code == 200
    check.equal(response.status_code, 200)


@pytest.mark.api
def test_login_sin_password():
    body = {
        "email": "eve.holt@reqres.in",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    #assert response.status_code == 400
    #assert body["error"] == "Missing password"

    check.equal(response.status_code, 400)
    check.equal(body["error"], "Missing password")

@pytest.mark.api
def test_login_sin_email():
    body = {
        "password": "cyslicka",
    }

    response = requests.post("https://reqres.in/api/login", headers=headers,json=body)

    body = response.json()
    #assert response.status_code == 400
    #assert body["error"] == "Missing email or username"

    check.equal(response.status_code, 400)
    check.equal(body["error"], "Missing email or username")

@pytest.mark.api
def test_create_user():
    body = {
        "name": "juan",
        "email": "juanmacabral9@gmail.com",
        "password": "pass123*"
    }

    response = requests.post("https://reqres.in/api/users", headers=headers,json=body)

    data = response.json()

    #assert response.status_code == 201
    check.equal(response.status_code,201)
    
    #assert body["email"].count("@") == 1
    check.equal(body["email"].count("@"),1)
    #assert "*" in body["password"]
    check.is_in("*",body["password"])

    #assert data["name"] == body["name"]
    check.equal(data["name"],body["name"])
    #assert data["email"] == body["email"]
    check.equal(data["email"],body["email"])

    #assert response.elapsed.total_seconds() < 1
    check.less(response.elapsed.total_seconds(),5)

@pytest.mark.api
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2",headers=headers)

    #assert response.status_code == 204
    check.equal(response.status_code, 204)

@pytest.mark.api
def test_get_user():
    response = requests.get("https://reqres.in/api/users/2",headers=headers)

   # assert response.status_code == 200
    check.equal(response.status_code, 200)
    print(response.elapsed.total_seconds())

   #assert response.elapsed.total_seconds() < 1, 
    check.less(response.elapsed.total_seconds(), 5, "El tiempo de ejecucion tardo mas de lo esperado")