import pytest
import requests


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user("alkurjdhvnfmdcy")
    assert user["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo_search = github_api.search_repo('Testing-Framework')
    # Hardcoded value of total commits count
    # assert repo_search['total_count'] == 46389
    assert 'googletest' in repo_search['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo_search = github_api.search_repo('kidsfyxnjnmwuhcy')
    assert repo_search['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api):
    repo_search = github_api.search_repo('j')
    assert repo_search['total_count'] != 0


@pytest.mark.api
def test_list_of_emoji_available(github_api):
    emoji_list = github_api.get_emoji_list()
    assert emoji_list.status_code == 200


@pytest.mark.api
def test_emoji_exists(github_api):
    emoji_list = github_api.get_emoji_list().json()
    assert "arrow_right" in emoji_list


@pytest.mark.api
def test_commit_for_repo_exists(github_api):
    commits = github_api.get_repo_commits('sadkoldun', 'testing-framework')
    assert len(commits) > 0


@pytest.mark.api
def test_commit_exists_in_html(github_api):
    commits = github_api.get_repo_commits('sadkoldun', 'testing-framework')
    commit_html = requests.get(commits[0]["html_url"])
    assert commit_html.status_code == 200


@pytest.mark.api
def test_commit_if_user_not_exists(github_api):
    commits = github_api.get_repo_commits('akguzdfo', 'testing-framework')

    assert commits["message"] == "Not Found"
