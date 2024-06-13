import pytest
import requests


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("alkurjdhvnfmdcy")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('Testing-Framework')
    assert r['total_count'] == 46389
    assert 'googletest' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('kidsfyxnjnmwuhcy')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api):
    r = github_api.search_repo('j')
    assert r['total_count'] != 0


@pytest.mark.api
def test_list_of_emoji_available(github_api):
    r = github_api.get_emoji_list()
    assert r.status_code == 200


@pytest.mark.api
def test_emoji_exists(github_api):
    r = github_api.get_emoji_list().json()
    assert "arrow_right" in r


@pytest.mark.api
def test_commit_for_repo_exists(github_api):
    body = github_api.get_repo_commits('sadkoldun', 'testing-framework')
    assert len(body) > 0


@pytest.mark.api
def test_commit_exists_in_html(github_api):
    body = github_api.get_repo_commits('sadkoldun', 'testing-framework')
    commit_html = requests.get(body[0]["html_url"])
    assert commit_html.status_code == 200


@pytest.mark.api
def test_commit_if_user_not_exists(github_api):
    body = github_api.get_repo_commits('akguzdfo', 'testing-framework')

    assert body["message"] == "Not Found"
