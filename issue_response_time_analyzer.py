def fetch_issues(owner, repo, state='all', token=None):
    """Fetch issues from the repo."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {"Authorization": f"token {token}"} if token else {}
    params = {"state": state, "per_page": 100}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        print("Failed to fetch issues.")
        return []

def get_first_response_time(issue):
    """Get the time to first response for an issue."""
    if not issue.get("comments"):
        return None
    import requests
    comments_url = issue["comments_url"]
    resp = requests.get(comments_url)
    if resp.status_code == 200:
        comments = resp.json()
        if comments:
            created = issue["created_at"]
            first_comment = comments[0]["created_at"]
            from dateutil import parser
            delta = parser.parse(first_comment) - parser.parse(created)
            return delta.total_seconds() / 3600  # hours
    return None

