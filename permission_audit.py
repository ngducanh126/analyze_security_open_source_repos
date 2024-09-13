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

def list_read_access(owner, repo, token=None):
    """List users with read permission."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/collaborators"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for user in resp.json():
            if user.get("permissions", {}).get("pull"):
                print(f"Read access: {user['login']}")
    else:
        print("Failed to fetch collaborators.")

def check_branch_protection(owner, repo, branch, token=None):
    """Check if a branch is protected."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/branches/{branch}/protection"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        print(f"Branch {branch} is protected.")
    else:
        print(f"Branch {branch} is not protected or failed to fetch.")

def list_forks(owner, repo, token=None):
    """List all forks of a repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/forks"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for fork in resp.json():
            print(f"Fork: {fork['full_name']}")
    else:
        print("Failed to fetch forks.")

def list_repo_invitations(owner, repo, token=None):
    """List pending invitations to the repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/invitations"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for invite in resp.json():
            print(f"Invitation: {invite['invitee']['login']}")
    else:
        print("Failed to fetch invitations.")

def check_team_permissions(owner, repo, token=None):
    """List teams and their permissions for a repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/teams"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for team in resp.json():
            print(f"Team: {team['name']}, Permission: {team['permission']}")
    else:
        print("Failed to fetch teams.")

def check_repo_visibility(owner, repo, token=None):
    """Check if the repo is internal, private, or public."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        print(f"Visibility: {data.get('visibility', 'unknown')}")
    else:
        print("Failed to fetch repo info.")

def list_dependabot_alerts(owner, repo, token=None):
    """List Dependabot alerts for a repo (requires special permissions)."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/dependabot/alerts"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for alert in resp.json():
            print(f"Dependabot alert: {alert['dependency']['package']['name']}")
    else:
        print("Failed to fetch Dependabot alerts or insufficient permissions.")

