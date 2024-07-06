import pytest
import requests


@pytest.mark.http
def test_first_request():
    response = requests.get("https://api.github.com/zen")
    print(response.text)


@pytest.mark.http
def test_second_request():
    response = requests.get("https://api.github.com/users/defunkt")
    body = response.json()
    headers = response.headers
    assert body['id'] == 2
    assert response.status_code == 200
    assert headers['Server'].lower() == "github.com"


@pytest.mark.http
def test_404_request():
    response = requests.get("https://api.github.com/users/jaba_oleg")

    assert response.status_code == 404
