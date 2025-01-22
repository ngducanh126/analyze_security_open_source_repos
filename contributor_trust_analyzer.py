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

def contributor_touched_critical(owner, repo, contributor, token=None):
    commits = get_contributor_commits(owner, repo, contributor, token)
    critical = get_critical_files()
    for commit in commits:
        files_url = commit["url"] + "/files"
        import requests
        headers = {"Authorization": f"token {token}"} if token else {}
        resp = requests.get(files_url, headers=headers)
        if resp.status_code == 200:
            files = [f["filename"] for f in resp.json()]
            if any(any(c in f for c in critical) for f in files):
                return True
    return False

