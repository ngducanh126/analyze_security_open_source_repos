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

