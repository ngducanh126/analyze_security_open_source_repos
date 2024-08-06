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

def fetch_security_advisories(owner, repo):
    """Fetch security advisories for the repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/security/advisories"
    resp = requests.get(url)
    if resp.status_code == 200:
        advisories = resp.json()
        print(f"Security advisories: {len(advisories)}")
        for adv in advisories:
            print(f"- {adv.get('summary', 'No summary')}")
    else:
        print("Failed to fetch advisories.")

def check_security_md(owner, repo):
    """Check if SECURITY.md exists in the repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/SECURITY.md"
    resp = requests.get(url)
    if resp.status_code == 200:
        print("SECURITY.md exists.")
    else:
        print("SECURITY.md not found.")

def fetch_recent_security_commits(owner, repo):
    """Fetch recent commits mentioning security."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {'per_page': 100}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        commits = resp.json()
        sec_commits = [c for c in commits if 'security' in c['commit']['message'].lower()]
        print(f"Recent security commits: {len(sec_commits)}")
        for c in sec_commits:
            print(f"- {c['commit']['message'].splitlines()[0]}")
    else:
        print("Failed to fetch commits.")

def fetch_security_labels(owner, repo):
    """List all labels containing 'security'."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/labels"
    resp = requests.get(url)
    if resp.status_code == 200:
        labels = resp.json()
        sec_labels = [l['name'] for l in labels if 'security' in l['name'].lower()]
        print(f"Security-related labels: {sec_labels}")
    else:
        print("Failed to fetch labels.")

def fetch_security_releases(owner, repo):
    """Fetch releases mentioning security."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    resp = requests.get(url)
    if resp.status_code == 200:
        releases = resp.json()
        sec_releases = [r for r in releases if 'security' in (r.get('body') or '').lower()]
        print(f"Releases mentioning security: {len(sec_releases)}")
        for r in sec_releases:
            print(f"- {r['tag_name']}: {r['name']}")
    else:
        print("Failed to fetch releases.")

