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

def print_bandit_summary(bandit_json):
    summary = summarize_bandit_findings(bandit_json)
    for code, count in summary.items():
        print(f"{code}: {count} findings")

def list_high_severity_issues(bandit_json):
    if not bandit_json or "results" not in bandit_json:
        return []
    return [f for f in bandit_json["results"] if f["issue_severity"] == "HIGH"]

def list_medium_severity_issues(bandit_json):
    if not bandit_json or "results" not in bandit_json:
        return []
    return [f for f in bandit_json["results"] if f["issue_severity"] == "MEDIUM"]

