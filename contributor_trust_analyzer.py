def list_contributors(owner, repo, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return []

def get_contributor_commits(owner, repo, contributor, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {token}"} if token else {}
    params = {"author": contributor, "per_page": 100}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        return resp.json()
    return []

def get_critical_files():
    return ["setup.py", "requirements.txt", ".github/workflows/", "src/", "main.py"]

