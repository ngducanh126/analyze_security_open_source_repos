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

def find_env_var_exports_in_code(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".sh"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if line.strip().startswith("export ") and ("SECRET" in line or "TOKEN" in line):
                            found.append((path, i+1, line.strip()))
    return found

def find_env_var_logging(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "os.environ" in line and ("print" in line or "logging" in line):
                            found.append((path, i+1, line.strip()))
    return found

def find_env_var_in_config_files(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".env") or f.endswith(".yml") or f.endswith(".yaml"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "SECRET" in line or "TOKEN" in line:
                            found.append((path, i+1, line.strip()))
    return found

def find_env_var_in_dockerfiles(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.lower() == "dockerfile":
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "ENV" in line and ("SECRET" in line or "TOKEN" in line):
                            found.append((path, i+1, line.strip()))
    return found

def find_env_var_in_tests(directory):
    import os
    found = []
    if os.path.exists("tests"):
        for root, dirs, files in os.walk("tests"):
            for f in files:
                if f.endswith(".py"):
                    path = os.path.join(root, f)
                    with open(path, "r", encoding="utf-8") as file:
                        for i, line in enumerate(file):
                            if "os.environ" in line:
                                found.append((path, i+1, line.strip()))
    return found

def find_env_var_in_examples(directory):
    import os
    found = []
    if os.path.exists("examples"):
        for root, dirs, files in os.walk("examples"):
            for f in files:
                if f.endswith(".py"):
                    path = os.path.join(root, f)
                    with open(path, "r", encoding="utf-8") as file:
                        for i, line in enumerate(file):
                            if "os.environ" in line:
                                found.append((path, i+1, line.strip()))
    return found

def find_env_var_in_docs(directory):
    import os
    found = []
    if os.path.exists("docs"):
        for root, dirs, files in os.walk("docs"):
            for f in files:
                if f.endswith(".md") or f.endswith(".rst"):
                    path = os.path.join(root, f)
                    with open(path, "r", encoding="utf-8") as file:
                        for i, line in enumerate(file):
                            if "SECRET" in line or "TOKEN" in line:
                                found.append((path, i+1, line.strip()))
    return found

def print_env_var_usage_report(directory):
    print("Python code:", find_env_var_usage_in_code(directory))
    print("Shell exports:", find_env_var_exports_in_code(directory))
    print("Logging env vars:", find_env_var_logging(directory))
    print("Config files:", find_env_var_in_config_files(directory))
    print("Dockerfiles:", find_env_var_in_dockerfiles(directory))
    print("Tests:", find_env_var_in_tests(directory))
    print("Examples:", find_env_var_in_examples(directory))
    print("Docs:", find_env_var_in_docs(directory))

