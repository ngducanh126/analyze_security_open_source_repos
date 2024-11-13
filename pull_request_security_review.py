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

def pr_merged_time(owner, repo, pr_number, token=None):
    import requests
    from dateutil import parser
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        pr = resp.json()
        if pr.get("merged_at"):
            created = parser.parse(pr["created_at"])
            merged = parser.parse(pr["merged_at"])
            print(f"PR #{pr_number} merged in {(merged - created).total_seconds() / 3600:.2f} hours")
        else:
            print(f"PR #{pr_number} not merged.")
    else:
        print(f"Failed to fetch PR #{pr_number}.")

def pr_closed_without_merge(owner, repo, token=None):
    prs = fetch_pull_requests(owner, repo, state='closed', token=token)
    closed = [pr['number'] for pr in prs if not pr.get('merged_at')]
    print(f"PRs closed without merge: {closed}")

def pr_with_security_patch(owner, repo, token=None):
    prs = fetch_pull_requests(owner, repo, state='all', token=token)
    keywords = ['security', 'vulnerability', 'cve', 'exploit', 'patch']
    patched = [pr['number'] for pr in prs if any(k in (pr['title'] + pr.get('body', '')).lower() for k in keywords)]
    print(f"PRs patching security: {patched}")

def pr_review_time(owner, repo, pr_number, token=None):
    import requests
    from dateutil import parser
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        reviews = resp.json()
        if reviews:
            pr_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
            pr_resp = requests.get(pr_url, headers=headers)
            if pr_resp.status_code == 200:
                pr = pr_resp.json()
                created = parser.parse(pr["created_at"])
                first_review = parser.parse(reviews[0]["submitted_at"])
                print(f"PR #{pr_number} first reviewed in {(first_review - created).total_seconds() / 3600:.2f} hours")
        else:
            print(f"PR #{pr_number} has no reviews.")
    else:
        print(f"Failed to fetch reviews for PR #{pr_number}.")

def pr_security_reviewers(owner, repo, pr_number, token=None):
    reviews = fetch_pr_reviews(owner, repo, pr_number, token=token)
    keywords = ['security', 'vulnerability', 'exploit', 'patch']
    reviewers = set()
    for r in reviews:
        if any(k in (r.get('body') or '').lower() for k in keywords):
            reviewers.add(r['user']['login'])
    print(f"Security reviewers for PR #{pr_number}: {list(reviewers)}")

def pr_security_review_labels(owner, repo, pr_number, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/labels"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        labels = [l['name'] for l in resp.json() if 'security' in l['name'].lower()]
        print(f"Security labels for PR #{pr_number}: {labels}")
    else:
        print(f"Failed to fetch labels for PR #{pr_number}.")

def pr_security_review_time_stats(owner, repo, token=None):
    prs = fetch_pull_requests(owner, repo, state='all', token=token)
    times = []
    for pr in prs:
        if any('security' in l['name'].lower() for l in pr.get('labels', [])):
            import requests
            from dateutil import parser
            url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr['number']}/reviews"
            headers = {"Authorization": f"token {token}"} if token else {}
            resp = requests.get(url, headers=headers)
            if resp.status_code == 200:
                reviews = resp.json()
                if reviews:
                    created = parser.parse(pr["created_at"])
                    first_review = parser.parse(reviews[0]["submitted_at"])
                    times.append((first_review - created).total_seconds() / 3600)
    if times:
        avg = sum(times) / len(times)
        print(f"Average time to review security PRs: {avg:.2f} hours")
    else:
        print("No security PRs with review times found.")


if __name__ == "__main__":
    owner = "octocat"
    repo = "Hello-World"
    token = None

    print("Security-labelled PRs:")
    security_labelled_prs(owner, repo, token)

