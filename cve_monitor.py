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

def fetch_cves_from_osv(owner, repo):
    """Fetch CVEs from OSV.dev for the repo."""
    import requests
    url = "https://api.osv.dev/v1/query"
    data = {"repo": f"github.com/{owner}/{repo}"}
    resp = requests.post(url, json=data)
    if resp.status_code == 200:
        vulns = resp.json().get("vulns", [])
        for v in vulns:
            print(f"OSV: {v.get('id', 'N/A')} - {v.get('summary', '')}")
    else:
        print("Failed to fetch OSV vulnerabilities.")

