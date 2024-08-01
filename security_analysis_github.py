def fetch_open_security_issues(owner, repo):
    """Fetch open issues labeled as security."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {'state': 'open', 'labels': 'security', 'per_page': 100}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        issues = resp.json()
        print(f"Open security issues: {len(issues)}")
        for issue in issues:
            print(f"- #{issue['number']}: {issue['title']}")
    else:
        print("Failed to fetch issues.")

def fetch_closed_security_issues(owner, repo):
    """Fetch closed issues labeled as security."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {'state': 'closed', 'labels': 'security', 'per_page': 100}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        issues = resp.json()
        print(f"Closed security issues: {len(issues)}")
        for issue in issues:
            print(f"- #{issue['number']}: {issue['title']}")
    else:
        print("Failed to fetch issues.")

def fetch_security_prs(owner, repo):
    """Fetch pull requests with security in the title."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    params = {'state': 'all', 'per_page': 100}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        prs = resp.json()
        sec_prs = [pr for pr in prs if 'security' in pr['title'].lower()]
        print(f"Security-related PRs: {len(sec_prs)}")
        for pr in sec_prs:
            print(f"- #{pr['number']}: {pr['title']}")
    else:
        print("Failed to fetch PRs.")

def fetch_recent_cve_mentions(owner, repo):
    """Search for recent CVE mentions in issues and PRs."""
    import requests
    url = "https://api.github.com/search/issues"
    params = {'q': f'repo:{owner}/{repo} CVE', 'per_page': 50}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        items = resp.json().get('items', [])
        print(f"CVE mentions: {len(items)}")
        for item in items:
            print(f"- #{item['number']}: {item['title']}")
    else:
        print("Failed to search for CVEs.")

