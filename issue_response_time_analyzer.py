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

def average_first_response_time(owner, repo, token=None):
    """Calculate average first response time for issues."""
    issues = fetch_issues(owner, repo, state='all', token=token)
    times = []
    for issue in issues:
        t = get_first_response_time(issue)
        if t is not None:
            times.append(t)
    if times:
        avg = sum(times) / len(times)
        print(f"Average first response time: {avg:.2f} hours")
    else:
        print("No response times found.")

def get_time_to_close(issue):
    """Get the time to close for an issue."""
    if issue.get("closed_at"):
        from dateutil import parser
        created = parser.parse(issue["created_at"])
        closed = parser.parse(issue["closed_at"])
        return (closed - created).total_seconds() / 3600  # hours
    return None

def average_time_to_close(owner, repo, token=None):
    """Calculate average time to close for issues."""
    issues = fetch_issues(owner, repo, state='closed', token=token)
    times = []
    for issue in issues:
        t = get_time_to_close(issue)
        if t is not None:
            times.append(t)
    if times:
        avg = sum(times) / len(times)
        print(f"Average time to close: {avg:.2f} hours")
    else:
        print("No closed issues found.")

def fastest_response_issue(owner, repo, token=None):
    """Find the issue with the fastest first response."""
    issues = fetch_issues(owner, repo, state='all', token=token)
    min_time = None
    min_issue = None
    for issue in issues:
        t = get_first_response_time(issue)
        if t is not None and (min_time is None or t < min_time):
            min_time = t
            min_issue = issue
    if min_issue:
        print(f"Fastest response: {min_time:.2f} hours for issue #{min_issue['number']}")
    else:
        print("No issues with responses found.")

def slowest_response_issue(owner, repo, token=None):
    """Find the issue with the slowest first response."""
    issues = fetch_issues(owner, repo, state='all', token=token)
    max_time = None
    max_issue = None
    for issue in issues:
        t = get_first_response_time(issue)
        if t is not None and (max_time is None or t > max_time):
            max_time = t
            max_issue = issue
    if max_issue:
        print(f"Slowest response: {max_time:.2f} hours for issue #{max_issue['number']}")
    else:
        print("No issues with responses found.")

def issues_without_response(owner, repo, token=None):
    """List issues with no response."""
    issues = fetch_issues(owner, repo, state='open', token=token)
    no_response = [issue for issue in issues if not issue.get("comments")]
    print(f"Issues with no response: {[i['number'] for i in no_response]}")

def issues_closed_without_response(owner, repo, token=None):
    """List closed issues with no response."""
    issues = fetch_issues(owner, repo, state='closed', token=token)
    no_response = [issue for issue in issues if not issue.get("comments")]
    print(f"Closed issues with no response: {[i['number'] for i in no_response]}")

def median_first_response_time(owner, repo, token=None):
    """Calculate median first response time for issues."""
    import statistics
    issues = fetch_issues(owner, repo, state='all', token=token)
    times = [get_first_response_time(issue) for issue in issues if get_first_response_time(issue) is not None]
    if times:
        median = statistics.median(times)
        print(f"Median first response time: {median:.2f} hours")
    else:
        print("No response times found.")

