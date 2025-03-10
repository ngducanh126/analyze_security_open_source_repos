def find_binary_files(directory):
    import os
    exts = [".exe", ".dll", ".so", ".dylib", ".bin", ".o", ".a"]
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if any(f.lower().endswith(e) for e in exts):
                found.append(os.path.join(root, f))
    return found

