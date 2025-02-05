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

