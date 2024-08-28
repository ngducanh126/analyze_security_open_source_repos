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

def detect_pickle_usage(repo_path):
    """Detect usage of pickle module (unsafe deserialization)."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "pickle." in line:
                            print(f"pickle usage found in {file} at line {i}: {line.strip()}")

def detect_yaml_load_usage(repo_path):
    """Detect unsafe yaml.load usage (should use safe_load)."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "yaml.load(" in line and "safe_load" not in line:
                            print(f"yaml.load() found in {file} at line {i}: {line.strip()}")

def detect_input_usage(repo_path):
    """Detect usage of input() in Python files (may be dangerous in some contexts)."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "input(" in line:
                            print(f"input() found in {file} at line {i}: {line.strip()}")

def detect_shell_true_subprocess(repo_path):
    """Detect subprocess calls with shell=True."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "subprocess" in line and "shell=True" in line:
                            print(f"subprocess with shell=True in {file} at line {i}: {line.strip()}")

def detect_javascript_eval(repo_path):
    """Detect eval() usage in JavaScript files."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.js'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "eval(" in line:
                            print(f"eval() found in {file} at line {i}: {line.strip()}")

def detect_javascript_function_constructor(repo_path):
    """Detect Function constructor usage in JavaScript files."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.js'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "new Function(" in line:
                            print(f"Function constructor found in {file} at line {i}: {line.strip()}")

def detect_php_eval(repo_path):
    """Detect eval() usage in PHP files."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.php'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if "eval(" in line:
                            print(f"eval() found in {file} at line {i}: {line.strip()}")

def detect_php_system_calls(repo_path):
    """Detect system/exec/passthru/shell_exec usage in PHP files."""
    import os
    dangerous = ["system(", "exec(", "passthru(", "shell_exec("]
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.php'):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        for d in dangerous:
                            if d in line:
                                print(f"{d.strip('(')} found in {file} at line {i}: {line.strip()}")

