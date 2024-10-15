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

def fetch_cve_details(cve_id):
    """Fetch details for a specific CVE."""
    import requests
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    resp = requests.get(url)
    if resp.status_code == 200:
        cve = resp.json()
        print(f"{cve['id']}: {cve['summary']}")
        print("CVSS:", cve.get("cvss", "N/A"))
    else:
        print("Failed to fetch CVE details.")

def fetch_nvd_cve_feed():
    """Fetch the latest NVD CVE feed (summary only)."""
    import requests
    url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    resp = requests.get(url)
    if resp.status_code == 200:
        for item in resp.json().get("result", {}).get("CVE_Items", []):
            cve_id = item["cve"]["CVE_data_meta"]["ID"]
            desc = item["cve"]["description"]["description_data"][0]["value"]
            print(f"{cve_id}: {desc}")
    else:
        print("Failed to fetch NVD CVE feed.")

def fetch_cves_for_language(language):
    """Fetch CVEs for a programming language ecosystem from OSV.dev."""
    import requests
    url = "https://api.osv.dev/v1/query"
    data = {"ecosystem": language}
    resp = requests.post(url, json=data)
    if resp.status_code == 200:
        vulns = resp.json().get("vulns", [])
        for v in vulns:
            print(f"{language} CVE: {v.get('id', 'N/A')} - {v.get('summary', '')}")
    else:
        print("Failed to fetch language vulnerabilities.")

def fetch_cves_for_commit(owner, repo, commit_hash):
    """Check if a commit is referenced in any CVE advisory."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/commits/{commit_hash}/pulls"
    headers = {"Accept": "application/vnd.github.groot-preview+json"}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        for pr in resp.json():
            if "cve" in pr["title"].lower():
                print(f"CVE-related PR: {pr['title']}")
    else:
        print("Failed to fetch commit PRs.")

def fetch_cves_for_dependency(owner, repo, dependency):
    """Check if a dependency has known CVEs using OSV.dev."""
    import requests
    url = "https://api.osv.dev/v1/query"
    data = {"package": {"name": dependency}}
    resp = requests.post(url, json=data)
    if resp.status_code == 200:
        vulns = resp.json().get("vulns", [])
        for v in vulns:
            print(f"Dependency CVE: {v.get('id', 'N/A')} - {v.get('summary', '')}")
    else:
        print("Failed to fetch dependency vulnerabilities.")

def fetch_cves_for_github_release(owner, repo, release_tag):
    """Check if a GitHub release is associated with any CVE."""
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{release_tag}"
    resp = requests.get(url)
    if resp.status_code == 200:
        release = resp.json()
        if "cve" in (release.get("body") or "").lower():
            print(f"CVE mentioned in release {release_tag}")
        else:
            print(f"No CVE mentioned in release {release_tag}")
    else:
        print("Failed to fetch release info.")

def fetch_cves_for_year(year):
    """Fetch CVEs published in a specific year from cve.circl.lu."""
    import requests
    url = f"https://cve.circl.lu/api/cvefor/{year}"
    resp = requests.get(url)
    if resp.status_code == 200:
        for cve in resp.json():
            print(f"{cve['id']}: {cve['summary']}")
    else:
        print("Failed to fetch CVEs for year.")

def fetch_cves_for_vendor_product(vendor, product):
    """Fetch CVEs for a vendor/product from cve.circl.lu."""
    import requests
    url = f"https://cve.circl.lu/api/search/{vendor}/{product}"
    resp = requests.get(url)
    if resp.status_code == 200:
        for cve in resp.json().get("data", []):
            print(f"{cve['id']}: {cve['summary']}")
    else:
        print("Failed to fetch vendor/product CVEs.")

def fetch_cve_references(cve_id):
    """Fetch references for a specific CVE."""
    import requests
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    resp = requests.get(url)
    if resp.status_code == 200:
        cve = resp.json()
        for ref in cve.get("references", []):
            print(f"Reference: {ref}")
    else:
        print("Failed to fetch CVE references.")

def fetch_cve_cvss_score(cve_id):
    """Fetch CVSS score for a specific CVE."""
    import requests
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    resp = requests.get(url)
    if resp.status_code == 200:
        cve = resp.json()
        print(f"CVSS score for {cve_id}: {cve.get('cvss', 'N/A')}")
    else:
        print("Failed to fetch CVSS score.")

def fetch_cve_published_date(cve_id):
    """Fetch published date for a specific CVE."""
    import requests
    url = f"https://cve.circl.lu/api/cve/{cve_id}"
    resp = requests.get(url)
    if resp.status_code == 200:
        cve = resp.json()
        print(f"Published date for {cve_id}: {cve.get('Published', 'N/A')}")
    else:
        print("Failed to fetch published date.")

