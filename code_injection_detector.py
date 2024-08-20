def detect_eval_usage(repo_path):
    """Detect usage of eval() in Python files."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "eval(" in line:
                            print(f"eval() found in {file} at line {i}: {line.strip()}")

def detect_exec_usage(repo_path):
    """Detect usage of exec() in Python files."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "exec(" in line:
                            print(f"exec() found in {file} at line {i}: {line.strip()}")

def detect_os_system_usage(repo_path):
    """Detect usage of os.system() in Python files."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "os.system(" in line:
                            print(f"os.system() found in {file} at line {i}: {line.strip()}")

def detect_subprocess_usage(repo_path):
    """Detect usage of subprocess module in Python files."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "subprocess." in line:
                            print(f"subprocess usage found in {file} at line {i}: {line.strip()}")

