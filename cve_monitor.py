def fetch_repo_cves(owner, repo):
    """Fetch CVEs related to the repo from GitHub Advisory Database."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/security/advisories"
    resp = requests.get(url)
    if resp.status_code == 200:
        advisories = resp.json()
        for adv in advisories:
            print(f"CVE: {adv.get('cve_id', 'N/A')} - {adv.get('summary', '')}")
    else:
        print("Failed to fetch advisories.")

