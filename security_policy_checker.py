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

def fetch_security_md_content(owner, repo, token=None):
    """Fetch and print the content of SECURITY.md if it exists."""
    import requests, base64
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        content = base64.b64decode(resp.json()['content']).decode('utf-8')
        print(content)
    else:
        print("SECURITY.md not found.")

def check_security_policy_section(owner, repo, token=None):
    """Check if SECURITY.md contains a policy section."""
    import requests, base64
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        content = base64.b64decode(resp.json()['content']).decode('utf-8').lower()
        print("Policy section found." if "policy" in content else "No policy section found.")
    else:
        print("SECURITY.md not found.")

