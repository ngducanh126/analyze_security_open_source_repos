def detect_license_file(owner, repo, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/license"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("license", {}).get("spdx_id", None)
    return None

def fetch_license_text(owner, repo, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/license"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        import base64
        return base64.b64decode(resp.json()["content"]).decode("utf-8")
    return None

def check_license_compatibility(license_id, allowed_licenses=None):
    if allowed_licenses is None:
        allowed_licenses = ["MIT", "Apache-2.0", "BSD-3-Clause"]
    return license_id in allowed_licenses

def list_dependency_licenses(requirements_file):
    licenses = []
    with open(requirements_file, "r", encoding="utf-8") as f:
        for line in f:
            pkg = line.strip().split("==")[0]
            lic = get_pypi_license(pkg)
            licenses.append((pkg, lic))
    return licenses

