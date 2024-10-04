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

def fetch_cves_for_package(package_name):
    """Fetch CVEs for a package from OSV.dev."""
    import requests
    url = "https://api.osv.dev/v1/query"
    data = {"package": {"name": package_name}}
    resp = requests.post(url, json=data)
    if resp.status_code == 200:
        vulns = resp.json().get("vulns", [])
        for v in vulns:
            print(f"Package CVE: {v.get('id', 'N/A')} - {v.get('summary', '')}")
    else:
        print("Failed to fetch package vulnerabilities.")

def fetch_recent_cves():
    """Fetch recent CVEs from cve.circl.lu."""
    import requests
    url = "https://cve.circl.lu/api/last"
    resp = requests.get(url)
    if resp.status_code == 200:
        for cve in resp.json():
            print(f"{cve['id']}: {cve['summary']}")
    else:
        print("Failed to fetch recent CVEs.")

