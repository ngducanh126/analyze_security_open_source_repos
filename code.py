import requests
from collections import Counter
from datetime import datetime


# Constants for GitHub API
GITHUB_API_BASE_URL = "https://api.github.com"
REPO_OWNER = "freeCodeCamp"
REPO_NAME = "freeCodeCamp"
SECURITY_KEYWORDS = ["security", "vulnerability", "exploit", "fix", "patch", "csrf", "xss", "sql injection", "threat", "password", "safe", "safety" , "ssh", "token"]


# fetch data from GitHub API
def fetch_github_data(url, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# get general repo info
def get_repo_info(owner, repo):
    repo_url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}"
    repo_info = fetch_github_data(repo_url)

    print(f"Repository: {repo_info['full_name']}")
    print(f"Description: {repo_info['description']}")
    print(f"Stars: {repo_info['stargazers_count']}")
    print(f"Forks: {repo_info['forks_count']}")
    print(f"Watchers: {repo_info['watchers_count']}")
    print(f"Primary language: {repo_info['language']}")


def analyze_commits(owner, repo):
    commits_url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/commits"
    params = {'per_page': 100}
    commits = fetch_github_data(commits_url, params)

    authors = Counter()
    dates = []
    for commit in commits:
        author = commit['commit']['author']['name']
        authors[author] += 1
        dates.append(datetime.strptime(commit['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ"))

    print(f"Total commits analyzed: {len(commits)}")
    print(f"Top 5 contributors:")
    for author, count in authors.most_common(5):
        print(f"  {author}: {count} commits")
    print(f"Oldest commit: {min(dates)}")
    print(f"Most recent commit: {max(dates)}")

# Function to analyze issues
def analyze_issues(owner, repo):
    issues_url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues"
    params = {'state': 'all', 'per_page': 100}
    issues = fetch_github_data(issues_url, params)

    open_issues = sum(1 for issue in issues if issue['state'] == 'open')
    closed_issues = sum(1 for issue in issues if issue['state'] == 'closed')

    print(f"Total issues analyzed: {len(issues)}")
    print(f"Open issues: {open_issues}")
    print(f"Closed issues: {closed_issues}")

# Function to analyze pull requests
def analyze_pull_requests(owner, repo):
    pulls_url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/pulls"
    params = {'state': 'all', 'per_page': 100}
    pulls = fetch_github_data(pulls_url, params)

    open_prs = sum(1 for pr in pulls if pr['state'] == 'open')
    closed_prs = sum(1 for pr in pulls if pr['state'] == 'closed')

    print(f"Total pull requests analyzed: {len(pulls)}")
    print(f"Open pull requests: {open_prs}")
    print(f"Closed pull requests: {closed_prs}")


# search for security mentions in commits
def search_commits_for_security(owner, repo):
    # still need to fix
    commits_url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/commits"
    params = {'per_page': 100}
    commits = fetch_github_data(commits_url, params)

    security_commits = []
    for commit in commits:
        message = commit['commit']['message'].lower()
        if any(keyword in message for keyword in SECURITY_KEYWORDS):
            print('')
            security_commits.append(commit)

    return security_commits


# search for security mentions in commits in PR
def search_issues_and_prs_for_security(owner, repo):
    #still need to fix
    issues_url = f"{GITHUB_API_BASE_URL}/search/issues"
    query = f"repo:{owner}/{repo} {' '.join(SECURITY_KEYWORDS)}"
    params = {'q': query, 'per_page': 100}

    issues_and_prs = fetch_github_data(issues_url, params)
    return issues_and_prs['items']



# MAIN FUNCTION TO ANALYZE REPO !!
try:
    # get general info
    print('Getting general information ')
    get_repo_info(REPO_OWNER, REPO_NAME)
    print('----------------')

    # Search commits
    print('SEARCHING COMMITS ')
    analyze_commits(REPO_OWNER, REPO_NAME)
    print('----------------')

    #search issues
    print('SEARCHING ISSUES')
    analyze_issues(REPO_OWNER, REPO_NAME)
    print('----------------')

    #serch PRs
    print('SEARCHING PRS')
    analyze_pull_requests(REPO_OWNER, REPO_NAME)

    #still need to fix function to find security mentions in commits and PR
except:
    print('error')

