import requests

# Constants for GitHub API
GITHUB_API_BASE_URL = "https://api.github.com"
REPO_OWNER = "freeCodeCamp"
REPO_NAME = "freeCodeCamp"
SECURITY_KEYWORDS = ["security", "vulnerability", "exploit", "fix", "patch", "csrf", "xss", "sql injection"]


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

# search for security mentions in commits
def search_commits_for_security(owner, repo):
    commits_url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/commits"
    params = {'per_page': 100}
    commits = fetch_github_data(commits_url, params)

    security_commits = []
    for commit in commits:
        message = commit['commit']['message'].lower()
        if any(keyword in message for keyword in SECURITY_KEYWORDS):
            security_commits.append(commit)

    return security_commits


# search for security mentions in commits in PR
def search_issues_and_prs_for_security(owner, repo):
    issues_url = f"{GITHUB_API_BASE_URL}/search/issues"
    query = f"repo:{owner}/{repo} {' '.join(SECURITY_KEYWORDS)}"
    params = {'q': query, 'per_page': 100}

    issues_and_prs = fetch_github_data(issues_url, params)
    return issues_and_prs['items']



# MAIN FUNCTION TO ANALYZE REPO !!
try:
    # get general info
    get_repo_info(REPO_OWNER, REPO_NAME)

    # Search commits
    security_commits = search_commits_for_security(REPO_OWNER, REPO_NAME)
    print("Found {len(security_commits)} security-related commits.")
    for commit in security_commits:
        print(f"Commit: {commit['sha']}, Message: {commit['commit']['message']}")

    # Search pull requests and issues
    security_issues_and_prs = search_issues_and_prs_for_security(REPO_OWNER, REPO_NAME)
    print(f"\nFound {len(security_issues_and_prs)} security-related pull requests and issues.")
    for item in security_issues_and_prs:
        print(f"Type: {'Pull Request' if 'pull_request' in item else 'Issue'}, Title: {item['title']}")

except:
    print('error')

