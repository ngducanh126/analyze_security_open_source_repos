def shannon_entropy(data):
    from math import log2
    if not data:
        return 0
    freq = {}
    for c in data:
        freq[c] = freq.get(c, 0) + 1
    entropy = 0
    for c in freq:
        p = freq[c] / len(data)
        entropy -= p * log2(p)
    return entropy

def is_high_entropy_string(s, threshold=4.5):
    return shannon_entropy(s) > threshold

def find_high_entropy_strings_in_file(filepath, threshold=4.5, min_length=20):
    found = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            for word in line.strip().split():
                if len(word) >= min_length and is_high_entropy_string(word, threshold):
                    found.append((i+1, word))
    return found

def scan_directory_for_high_entropy_strings(directory, threshold=4.5, min_length=20):
    import os
    results = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".py") or f.endswith(".env") or f.endswith(".txt"):
                path = os.path.join(root, f)
                res = find_high_entropy_strings_in_file(path, threshold, min_length)
                if res:
                    results.append((path, res))
    return results

def print_entropy_scan_report(directory):
    results = scan_directory_for_high_entropy_strings(directory)
    for path, items in results:
        print(f"{path}:")
        for line, word in items:
            print(f"  Line {line}: {word}")

def find_possible_secrets_in_file(filepath):
    found = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            if "key" in line.lower() or "secret" in line.lower() or "token" in line.lower():
                found.append((i+1, line.strip()))
    return found

def scan_directory_for_possible_secrets(directory):
    import os
    results = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".py") or f.endswith(".env") or f.endswith(".txt"):
                path = os.path.join(root, f)
                res = find_possible_secrets_in_file(path)
                if res:
                    results.append((path, res))
    return results

def print_possible_secrets_report(directory):
    results = scan_directory_for_possible_secrets(directory)
    for path, items in results:
        print(f"{path}:")
        for line, text in items:
            print(f"  Line {line}: {text}")

def find_high_entropy_env_vars(filepath, threshold=4.5, min_length=20):
    found = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            if "=" in line:
                key, val = line.strip().split("=", 1)
                if len(val) >= min_length and is_high_entropy_string(val, threshold):
                    found.append((i+1, key, val))
    return found

def scan_env_files_for_high_entropy(directory, threshold=4.5, min_length=20):
    import os
    results = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".env"):
                path = os.path.join(root, f)
                res = find_high_entropy_env_vars(path, threshold, min_length)
                if res:
                    results.append((path, res))
    return results

def print_env_entropy_report(directory):
    results = scan_env_files_for_high_entropy(directory)
    for path, items in results:
        print(f"{path}:")
        for line, key, val in items:
            print(f"  Line {line}: {key} = {val}")

