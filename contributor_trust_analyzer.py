def list_contributors(owner, repo, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return []

def get_contributor_commits(owner, repo, contributor, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {token}"} if token else {}
    params = {"author": contributor, "per_page": 100}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        return resp.json()
    return []

def get_critical_files():
    return ["setup.py", "requirements.txt", ".github/workflows/", "src/", "main.py"]

def contributor_touched_critical(owner, repo, contributor, token=None):
    commits = get_contributor_commits(owner, repo, contributor, token)
    critical = get_critical_files()
    for commit in commits:
        files_url = commit["url"] + "/files"
        import requests
        headers = {"Authorization": f"token {token}"} if token else {}
        resp = requests.get(files_url, headers=headers)
        if resp.status_code == 200:
            files = [f["filename"] for f in resp.json()]
            if any(any(c in f for c in critical) for f in files):
                return True
    return False

def list_new_contributors(owner, repo, days=30, token=None):
    import requests
    from datetime import datetime, timezone, timedelta
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    new_contributors = []
    if resp.status_code == 200:
        for user in resp.json():
            events_url = f"https://api.github.com/users/{user['login']}/events"
            events_resp = requests.get(events_url, headers=headers)
            if events_resp.status_code == 200:
                for event in events_resp.json():
                    if event["type"] == "PushEvent":
                        created = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                        if (datetime.now(timezone.utc) - created).days <= days:
                            new_contributors.append(user["login"])
                            break
    return new_contributors

def get_contributor_first_commit_date(owner, repo, contributor, token=None):
    commits = get_contributor_commits(owner, repo, contributor, token)
    if commits:
        from dateutil import parser
        dates = [parser.parse(c["commit"]["author"]["date"]) for c in commits]
        return min(dates)
    return None

def get_contributor_last_commit_date(owner, repo, contributor, token=None):
    commits = get_contributor_commits(owner, repo, contributor, token)
    if commits:
        from dateutil import parser
        dates = [parser.parse(c["commit"]["author"]["date"]) for c in commits]
        return max(dates)
    return None

def get_contributor_commit_count(owner, repo, contributor, token=None):
    commits = get_contributor_commits(owner, repo, contributor, token)
    return len(commits)

def get_contributor_files_changed(owner, repo, contributor, token=None):
    commits = get_contributor_commits(owner, repo, contributor, token)
    files = set()
    for commit in commits:
        files_url = commit["url"] + "/files"
        import requests
        headers = {"Authorization": f"token {token}"} if token else {}
        resp = requests.get(files_url, headers=headers)
        if resp.status_code == 200:
            for f in resp.json():
                files.add(f["filename"])
    return list(files)

def is_new_contributor(owner, repo, contributor, days=30, token=None):
    from datetime import datetime, timezone
    first_commit = get_contributor_first_commit_date(owner, repo, contributor, token)
    if first_commit:
        return (datetime.now(timezone.utc) - first_commit).days <= days
    return False

def list_critical_changes_by_new_contributors(owner, repo, token=None):
    new_contribs = list_new_contributors(owner, repo, token=token)
    critical = get_critical_files()
    result = []
    for user in new_contribs:
        files = get_contributor_files_changed(owner, repo, user, token)
        if any(any(c in f for c in critical) for f in files):
            result.append(user)
    return result

def print_contributor_trust_report(owner, repo, token=None):
    contributors = list_contributors(owner, repo, token)
    for user in contributors:
        name = user["login"]
        count = get_contributor_commit_count(owner, repo, name, token)
        new = is_new_contributor(owner, repo, name, token=token)
        print(f"{name}: {count} commits, {'NEW' if new else 'ESTABLISHED'}")

def print_critical_file_changes_by_new_contributors(owner, repo, token=None):
    users = list_critical_changes_by_new_contributors(owner, repo, token)
    for user in users:
        print(f"New contributor {user} changed critical files")

def print_all_contributor_files(owner, repo, token=None):
    contributors = list_contributors(owner, repo, token)
    for user in contributors:
        files = get_contributor_files_changed(owner, repo, user["login"], token)
        print(f"{user['login']}: {files}")

def print_contributor_activity_summary(owner, repo, token=None):
    contributors = list_contributors(owner, repo, token)
    for user in contributors:
        name = user["login"]
        first = get_contributor_first_commit_date(owner, repo, name, token)
        last = get_contributor_last_commit_date(owner, repo, name, token)
        print(f"{name}: first commit {first}, last commit {last}")

