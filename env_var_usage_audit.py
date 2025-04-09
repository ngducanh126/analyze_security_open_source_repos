def find_env_var_usage_in_code(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "os.environ" in line:
                            found.append((path, i+1, line.strip()))
    return found

