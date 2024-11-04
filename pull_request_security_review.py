def fetch_pull_requests(owner, repo, state='all', token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    headers = {"Authorization": f"token {token}"} if token else {}
    params = {"state": state, "per_page": 100}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Failed to fetch pull requests.")
        return []

def fetch_pr_reviews(owner, repo, pr_number, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"Failed to fetch reviews for PR #{pr_number}.")
        return []

def fetch_pr_comments(owner, repo, pr_number, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"Failed to fetch comments for PR #{pr_number}.")
        return []

def security_labelled_prs(owner, repo, token=None):
    prs = fetch_pull_requests(owner, repo, state='all', token=token)
    sec_prs = [pr for pr in prs if any('security' in l['name'].lower() for l in pr.get('labels', []))]
    print(f"Security-labelled PRs: {[pr['number'] for pr in sec_prs]}")

def pr_with_security_keywords(owner, repo, token=None):
    prs = fetch_pull_requests(owner, repo, state='all', token=token)
    keywords = ['security', 'vulnerability', 'cve', 'exploit', 'patch']
    sec_prs = [pr for pr in prs if any(k in (pr['title'] + pr.get('body', '')).lower() for k in keywords)]
    print(f"PRs with security keywords: {[pr['number'] for pr in sec_prs]}")

def pr_reviewed_by_security_team(owner, repo, pr_number, security_team, token=None):
    reviews = fetch_pr_reviews(owner, repo, pr_number, token=token)
    reviewed = any(r['user']['login'] in security_team for r in reviews)
    print(f"PR #{pr_number} reviewed by security team: {reviewed}")

def pr_with_security_review_comments(owner, repo, pr_number, token=None):
    reviews = fetch_pr_reviews(owner, repo, pr_number, token=token)
    keywords = ['security', 'vulnerability', 'exploit', 'patch']
    found = any(any(k in (r.get('body') or '').lower() for k in keywords) for r in reviews)
    print(f"PR #{pr_number} has security review comments: {found}")

