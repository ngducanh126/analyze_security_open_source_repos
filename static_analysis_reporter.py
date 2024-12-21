def run_bandit_on_directory(directory):
    import subprocess
    result = subprocess.run(["bandit", "-r", directory, "-f", "json"], capture_output=True, text=True)
    if result.returncode == 0:
        import json
        return json.loads(result.stdout)
    return None

def summarize_bandit_findings(bandit_json):
    if not bandit_json or "results" not in bandit_json:
        return {}
    summary = {}
    for finding in bandit_json["results"]:
        code = finding["test_id"]
        summary[code] = summary.get(code, 0) + 1
    return summary

