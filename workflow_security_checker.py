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

