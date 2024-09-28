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

def check_contact_info_in_security_md(owner, repo, token=None):
    """Check if SECURITY.md contains contact info."""
    import requests, base64, re
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        content = base64.b64decode(resp.json()['content']).decode('utf-8')
        if re.search(r'@|mailto:|http[s]?://', content):
            print("Contact info found in SECURITY.md.")
        else:
            print("No contact info in SECURITY.md.")
    else:
        print("SECURITY.md not found.")

def check_disclosure_instructions(owner, repo, token=None):
    """Check if SECURITY.md contains disclosure instructions."""
    import requests, base64
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        content = base64.b64decode(resp.json()['content']).decode('utf-8').lower()
        print("Disclosure instructions found." if "disclos" in content else "No disclosure instructions found.")
    else:
        print("SECURITY.md not found.")

def check_response_time_commitment(owner, repo, token=None):
    """Check if SECURITY.md mentions response time commitment."""
    import requests, base64, re
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        content = base64.b64decode(resp.json()['content']).decode('utf-8').lower()
        if re.search(r'respond|response time|within \d+ (hours|days)', content):
            print("Response time commitment found.")
        else:
            print("No response time commitment found.")
    else:
        print("SECURITY.md not found.")

def check_github_security_advisories_enabled(owner, repo, token=None):
    """Check if GitHub Security Advisories are enabled."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/security/advisories"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    print("Security advisories enabled." if resp.status_code == 200 else "Security advisories not enabled or insufficient permissions.")

def check_vulnerability_reporting(owner, repo, token=None):
    """Check if vulnerability reporting is mentioned in SECURITY.md."""
    import requests, base64
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        content = base64.b64decode(resp.json()['content']).decode('utf-8').lower()
        print("Vulnerability reporting instructions found." if "vulnerab" in content else "No vulnerability reporting instructions found.")
    else:
        print("SECURITY.md not found.")

def check_security_labels(owner, repo, token=None):
    """Check if repo has security-related labels."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/labels"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        labels = [l['name'] for l in resp.json() if 'security' in l['name'].lower()]
        print(f"Security labels: {labels}" if labels else "No security labels found.")
    else:
        print("Failed to fetch labels.")

def check_security_policy_link_in_readme(owner, repo, token=None):
    """Check if README links to SECURITY.md or security policy."""
    import requests, base64
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/README.md"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        content = base64.b64decode(resp.json()['content']).decode('utf-8').lower()
        print("Link to security policy found in README." if "security.md" in content or "security policy" in content else "No link to security policy in README.")
    else:
        print("README.md not found.")

def check_security_policy_in_docs(owner, repo, token=None):
    """Check if documentation mentions security policy."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/docs"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        files = [f['name'] for f in resp.json()]
        found = any('security' in name.lower() for name in files)
        print("Security policy found in docs." if found else "No security policy in docs.")
    else:
        print("Docs directory not found.")

def check_security_policy_last_updated(owner, repo, token=None):
    """Check when SECURITY.md was last updated."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"path": "SECURITY.md", "per_page": 1}
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200 and resp.json():
        print("SECURITY.md last updated at:", resp.json()[0]['commit']['committer']['date'])
    else:
        print("Could not determine last update for SECURITY.md.")

