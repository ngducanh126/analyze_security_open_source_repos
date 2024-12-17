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

def get_pypi_license(package):
    import requests
    url = f"https://pypi.org/pypi/{package}/json"
    resp = requests.get(url)
    if resp.status_code == 200:
        info = resp.json().get("info", {})
        return info.get("license", "Unknown")
    return "Unknown"

def check_all_dependencies_compatible(requirements_file, allowed_licenses=None):
    licenses = list_dependency_licenses(requirements_file)
    return [pkg for pkg, lic in licenses if not check_license_compatibility(lic, allowed_licenses)]

def check_license_badge_in_readme(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return "license" in content and "badge" in content

def check_license_years(license_file):
    with open(license_file, "r", encoding="utf-8") as f:
        content = f.read()
        import re
        return re.findall(r"20[0-9]{2}", content)

def check_license_holder(license_file):
    with open(license_file, "r", encoding="utf-8") as f:
        content = f.read()
        import re
        match = re.search(r"Copyright.*", content)
        if match:
            return match.group(0)
    return None

def check_license_header_in_files(directory):
    import os
    files = [f for f in os.listdir(directory) if f.endswith(".py")]
    result = []
    for file in files:
        with open(os.path.join(directory, file), "r", encoding="utf-8") as f:
            first = f.readline().lower()
            result.append((file, "copyright" in first or "license" in first))
    return result

def check_github_license_api(owner, repo, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/license"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    return resp.status_code == 200

def check_license_spdx(license_id):
    spdx = ["MIT", "Apache-2.0", "BSD-3-Clause", "GPL-3.0", "LGPL-3.0"]
    return license_id in spdx

def check_license_notice_in_dist(dist_file):
    with open(dist_file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return "license" in content

