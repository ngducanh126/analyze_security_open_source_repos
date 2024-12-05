def detect_license_file(owner, repo, token=None):
    import requests
    url = f"https://api.github.com/repos/{owner}/{repo}/license"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("license", {}).get("spdx_id", None)
    return None

