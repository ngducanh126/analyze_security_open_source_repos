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

