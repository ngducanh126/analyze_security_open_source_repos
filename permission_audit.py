def list_collaborators(owner, repo, token=None):
    """List all collaborators for a GitHub repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/collaborators"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for user in resp.json():
            print(f"Collaborator: {user['login']}")
    else:
        print("Failed to fetch collaborators.")

