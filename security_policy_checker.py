def check_security_md_exists(owner, repo, token=None):
    """Check if SECURITY.md exists in the repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    print("SECURITY.md found." if resp.status_code == 200 else "SECURITY.md not found.")

def check_security_md_in_github_dir(owner, repo, token=None):
    """Check if SECURITY.md exists in .github directory."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/.github/SECURITY.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    print(".github/SECURITY.md found." if resp.status_code == 200 else ".github/SECURITY.md not found.")

