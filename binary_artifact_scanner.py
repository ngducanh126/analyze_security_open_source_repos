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

