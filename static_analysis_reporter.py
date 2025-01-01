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

def list_low_severity_issues(bandit_json):
    if not bandit_json or "results" not in bandit_json:
        return []
    return [f for f in bandit_json["results"] if f["issue_severity"] == "LOW"]

def print_issue_details(issues):
    for issue in issues:
        print(f"{issue['filename']}:{issue['line_number']} {issue['issue_text']}")

def run_flake8_on_directory(directory):
    import subprocess
    result = subprocess.run(["flake8", directory, "--format=%(path)s:%(row)d:%(col)d: %(code)s %(text)s"], capture_output=True, text=True)
    return result.stdout.splitlines()

def summarize_flake8_issues(issues):
    summary = {}
    for issue in issues:
        code = issue.split(":")[3].split()[0]
        summary[code] = summary.get(code, 0) + 1
    return summary

def print_flake8_summary(issues):
    summary = summarize_flake8_issues(issues)
    for code, count in summary.items():
        print(f"{code}: {count} issues")

def run_safety_on_requirements(requirements_file):
    import subprocess
    result = subprocess.run(["safety", "check", "-r", requirements_file, "--json"], capture_output=True, text=True)
    if result.returncode == 0:
        import json
        return json.loads(result.stdout)
    return None

def summarize_safety_issues(safety_json):
    if not safety_json or not isinstance(safety_json, list):
        return 0
    return len(safety_json)

def print_safety_summary(safety_json):
    count = summarize_safety_issues(safety_json)
    print(f"Vulnerable dependencies: {count}")

