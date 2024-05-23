import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, repo_name):
        r = requests.get("https://api.github.com/search/repositories", params={'q': repo_name})
        body = r.json()

        return body

    def get_emoji_list(self):
        r = requests.get("https://api.github.com/emojis")

        return r

    def get_repo_commits(self, username, repo_name):
        r = requests.get(f"https://api.github.com/repos/{username}/{repo_name}/commits")
        body = r.json()

        return body
