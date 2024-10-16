def fetch_issues(owner, repo, state='all', token=None):
    """Fetch issues from the repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {"Authorization": f"token {token}"} if token else {}
    params = {"state": state, "per_page": 100}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Failed to fetch issues.")
        return []

