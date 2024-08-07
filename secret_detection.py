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

