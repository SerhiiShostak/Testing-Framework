import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers
    assert body['id'] == 2
    assert r.status_code == 200
    assert headers['Server'] == "GitHub.com"


@pytest.mark.http
def test_404_request():
    r = requests.get("https://api.github.com/users/jaba_oleg")

    assert r.status_code == 404
