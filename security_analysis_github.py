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

