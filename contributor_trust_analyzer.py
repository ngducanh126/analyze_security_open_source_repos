def list_contributors(owner, repo, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return []

