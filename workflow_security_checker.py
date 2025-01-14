def list_workflow_files(repo_path):
    import os
    workflows = []
    wf_dir = os.path.join(repo_path, ".github", "workflows")
    if os.path.isdir(wf_dir):
        for f in os.listdir(wf_dir):
            if f.endswith(".yml") or f.endswith(".yaml"):
                workflows.append(os.path.join(wf_dir, f))
    return workflows

def load_yaml_file(filepath):
    import yaml
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def find_unpinned_actions(workflow):
    unpinned = []
    if not workflow or "jobs" not in workflow:
        return unpinned
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            if "uses" in step and "@" not in step["uses"]:
                unpinned.append(step["uses"])
    return unpinned

def find_plaintext_secrets(workflow):
    secrets = []
    if not workflow or "jobs" not in workflow:
        return secrets
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            if "env" in step:
                for k, v in step["env"].items():
                    if isinstance(v, str) and ("secret" in v.lower() or "token" in v.lower()):
                        secrets.append((k, v))
    return secrets

def find_insecure_checkout(workflow):
    insecure = []
    if not workflow or "jobs" not in workflow:
        return insecure
    for job in workflow["jobs"].values():
        for step in job.get("uses", []):
            if "actions/checkout" in step and "@v1" in step:
                insecure.append(step)
    return insecure

def find_scripts_with_curl_bash(workflow):
    scripts = []
    if not workflow or "jobs" not in workflow:
        return scripts
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            if "run" in step and ("curl" in step["run"] and "| bash" in step["run"]):
                scripts.append(step["run"])
    return scripts

def find_open_permissions(workflow):
    open_perms = []
    if not workflow or "permissions" not in workflow:
        return open_perms
    if workflow["permissions"] == "write-all" or workflow["permissions"] == "read-all":
        open_perms.append(workflow["permissions"])
    return open_perms

def find_missing_permissions(workflow):
    missing = []
    if not workflow or "jobs" not in workflow:
        return missing
    for job_name, job in workflow["jobs"].items():
        if "permissions" not in job:
            missing.append(job_name)
    return missing

def find_actions_with_latest_tag(workflow):
    latest = []
    if not workflow or "jobs" not in workflow:
        return latest
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            if "uses" in step and step["uses"].endswith("@latest"):
                latest.append(step["uses"])
    return latest

def find_env_secrets_exposed(workflow):
    exposed = []
    if not workflow or "jobs" not in workflow:
        return exposed
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            if "env" in step:
                for k, v in step["env"].items():
                    if "SECRET" in k or "TOKEN" in k:
                        exposed.append((k, v))
    return exposed

def summarize_workflow_security(workflow):
    return {
        "unpinned_actions": find_unpinned_actions(workflow),
        "plaintext_secrets": find_plaintext_secrets(workflow),
        "insecure_checkout": find_insecure_checkout(workflow),
        "curl_bash": find_scripts_with_curl_bash(workflow),
        "open_permissions": find_open_permissions(workflow),
        "missing_permissions": find_missing_permissions(workflow),
        "latest_tag": find_actions_with_latest_tag(workflow),
        "env_secrets_exposed": find_env_secrets_exposed(workflow),
    }

