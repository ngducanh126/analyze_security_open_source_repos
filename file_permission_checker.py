def find_world_readable_files(directory):
    import os, stat
    result = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if os.path.isfile(path) and os.stat(path).st_mode & stat.S_IROTH:
                result.append(path)
    return result

def find_sensitive_files(directory):
    import os
    sensitive = [".env", "id_rsa", "id_dsa", "private.pem", "config.json", "secrets.yml"]
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f in sensitive:
                found.append(os.path.join(root, f))
    return found

def check_file_in_gitignore(filename):
    if not os.path.exists(".gitignore"):
        return False
    with open(".gitignore", "r", encoding="utf-8") as f:
        return filename in f.read()

def list_files_with_weak_permissions(directory):
    import os, stat
    weak = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            mode = os.stat(path).st_mode
            if mode & stat.S_IWOTH or mode & stat.S_IXOTH:
                weak.append(path)
    return weak

def find_private_keys(directory):
    import os
    keys = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".pem") or f.endswith(".key"):
                keys.append(os.path.join(root, f))
    return keys

def check_sensitive_files_committed(directory):
    import subprocess
    sensitive = [".env", "id_rsa", "id_dsa", "private.pem", "config.json", "secrets.yml"]
    result = []
    for s in sensitive:
        out = subprocess.run(["git", "ls-files", s], capture_output=True, text=True)
        if out.stdout.strip():
            result.append(s)
    return result

