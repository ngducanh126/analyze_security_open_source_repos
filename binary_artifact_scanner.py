def find_binary_files(directory):
    import os
    exts = [".exe", ".dll", ".so", ".dylib", ".bin", ".o", ".a"]
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if any(f.lower().endswith(e) for e in exts):
                found.append(os.path.join(root, f))
    return found

def check_binary_files_in_git(directory):
    import subprocess
    exts = [".exe", ".dll", ".so", ".dylib", ".bin", ".o", ".a"]
    result = []
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
    for line in out.stdout.splitlines():
        if any(line.lower().endswith(e) for e in exts):
            result.append(line)
    return result

def check_large_binary_files(directory, size_mb=5):
    import os
    exts = [".exe", ".dll", ".so", ".dylib", ".bin", ".o", ".a"]
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if any(f.lower().endswith(e) for e in exts) and os.path.getsize(path) > size_mb * 1024 * 1024:
                found.append(path)
    return found

def check_for_unsigned_binaries(directory):
    import os
    exts = [".exe", ".dll", ".so", ".dylib"]
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if any(f.lower().endswith(e) for e in exts):
                found.append(os.path.join(root, f))
    return found

def check_for_stripped_binaries(directory):
    import os, subprocess
    exts = [".so", ".dll", ".exe"]
    stripped = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if any(f.lower().endswith(e) for e in exts):
                path = os.path.join(root, f)
                out = subprocess.run(["file", path], capture_output=True, text=True)
                if "not stripped" in out.stdout:
                    stripped.append(path)
    return stripped

