def list_workflow_files(repo_path):
    import os
    workflows = []
    wf_dir = os.path.join(repo_path, ".github", "workflows")
    if os.path.isdir(wf_dir):
        for f in os.listdir(wf_dir):
            if f.endswith(".yml") or f.endswith(".yaml"):
                workflows.append(os.path.join(wf_dir, f))
    return workflows

