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

