def detect_aws_keys_in_files(repo_path):
    """Detect AWS Access Keys in files using regex."""
    import re, os
    aws_key_pattern = re.compile(r'AKIA[0-9A-Z]{16}')
    for root, _, files in os.walk(repo_path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if aws_key_pattern.search(line):
                            print(f"AWS key found in {file}: {line.strip()}")
            except Exception:
                continue

def detect_private_keys(repo_path):
    """Detect private key files by filename and content."""
    import os
    key_filenames = ['id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519', 'private.key']
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file in key_filenames:
                print(f"Possible private key file found: {os.path.join(root, file)}")
            else:
                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read(100)
                        if "PRIVATE KEY" in content:
                            print(f"Private key content found in: {os.path.join(root, file)}")
                except Exception:
                    continue

def detect_password_in_code(repo_path):
    """Detect hardcoded passwords in code files."""
    import re, os
    password_patterns = [re.compile(r'password\s*=\s*['\"]([^'\"]+)['\"]', re.I)]
    for root, _, files in os.walk(repo_path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        for pattern in password_patterns:
                            if pattern.search(line):
                                print(f"Hardcoded password found in {file}: {line.strip()}")
            except Exception:
                continue

def detect_api_keys(repo_path):
    """Detect generic API keys using regex patterns."""
    import re, os
    api_key_patterns = [
        re.compile(r'api[_-]?key\s*=\s*['\"]?[\w-]{16,}['\"]?', re.I),
        re.compile(r'slack[_-]?token\s*=\s*['\"]?xox[baprs]-[0-9a-zA-Z]{10,48}['\"]?', re.I)
    ]
    for root, _, files in os.walk(repo_path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        for pattern in api_key_patterns:
                            if pattern.search(line):
                                print(f"API key found in {file}: {line.strip()}")
            except Exception:
                continue

def detect_jwt_tokens(repo_path):
    """Detect JWT tokens in codebase."""
    import re, os
    jwt_pattern = re.compile(r'eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9._-]+\.[A-Za-z0-9._-]+')
    for root, _, files in os.walk(repo_path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if jwt_pattern.search(line):
                            print(f"JWT token found in {file}: {line.strip()}")
            except Exception:
                continue

def detect_secrets_in_git_history(repo_path):
    """Detect secrets in git history using git log and regex."""
    import subprocess, re
    secret_patterns = [re.compile(r'AKIA[0-9A-Z]{16}'), re.compile(r'password\s*=\s*['\"]([^'\"]+)['\"]', re.I)]
    try:
        log = subprocess.check_output(['git', '-C', repo_path, 'log', '-p', '-G', 'AKIA|password'], encoding='utf-8', errors='ignore')
        for line in log.splitlines():
            for pattern in secret_patterns:
                if pattern.search(line):
                    print(f"Secret found in git history: {line.strip()}")
    except Exception as e:
        print("Error scanning git history:", e)

def detect_env_secrets(repo_path):
    """Detect secrets in .env files."""
    import os
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file == ".env":
                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                        for line in f:
                            if "SECRET" in line or "KEY" in line or "PASSWORD" in line:
                                print(f"Possible secret in {file}: {line.strip()}")
                except Exception:
                    continue

def detect_github_tokens(repo_path):
    """Detect GitHub tokens in files."""
    import re, os
    github_token_pattern = re.compile(r'ghp_[A-Za-z0-9]{36,}')
    for root, _, files in os.walk(repo_path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if github_token_pattern.search(line):
                            print(f"GitHub token found in {file}: {line.strip()}")
            except Exception:
                continue

def detect_google_api_keys(repo_path):
    """Detect Google API keys in files."""
    import re, os
    google_api_pattern = re.compile(r'AIza[0-9A-Za-z-_]{35}')
    for root, _, files in os.walk(repo_path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        if google_api_pattern.search(line):
                            print(f"Google API key found in {file}: {line.strip()}")
            except Exception:
                continue

