def run_bandit_on_directory(directory):
    import subprocess
    result = subprocess.run(["bandit", "-r", directory, "-f", "json"], capture_output=True, text=True)
    if result.returncode == 0:
        import json
        return json.loads(result.stdout)
    return None

