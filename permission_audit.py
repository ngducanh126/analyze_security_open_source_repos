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

def list_teams(owner, repo, token=None):
    """List all teams with access to a GitHub repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/teams"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for team in resp.json():
            print(f"Team: {team['name']}")
    else:
        print("Failed to fetch teams.")

def check_public_access(owner, repo, token=None):
    """Check if a repo is public or private."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        print("Public" if not data.get("private", True) else "Private")
    else:
        print("Failed to fetch repo info.")

def list_outside_collaborators(owner, repo, token=None):
    """List outside collaborators (not in org) for a repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/collaborators"
    headers = {"Authorization": f"token {token}"} if token else {}
    params = {"affiliation": "outside"}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        for user in resp.json():
            print(f"Outside collaborator: {user['login']}")
    else:
        print("Failed to fetch outside collaborators.")

def list_admins(owner, repo, token=None):
    """List users with admin permission."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/collaborators"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for user in resp.json():
            if user.get("permissions", {}).get("admin"):
                print(f"Admin: {user['login']}")
    else:
        print("Failed to fetch collaborators.")

def list_write_access(owner, repo, token=None):
    """List users with write permission."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/collaborators"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for user in resp.json():
            if user.get("permissions", {}).get("push"):
                print(f"Write access: {user['login']}")
    else:
        print("Failed to fetch collaborators.")

