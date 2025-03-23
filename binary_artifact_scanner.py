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

def check_for_embedded_scripts_in_binaries(directory):
    import os
    exts = [".exe", ".dll", ".so", ".dylib"]
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if any(f.lower().endswith(e) for e in exts):
                path = os.path.join(root, f)
                with open(path, "rb") as file:
                    data = file.read()
                    if b"#!/bin" in data:
                        found.append(path)
    return found

def check_for_nonstandard_binaries(directory):
    import os
    exts = [".bin", ".dat", ".img"]
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if any(f.lower().endswith(e) for e in exts):
                found.append(os.path.join(root, f))
    return found

def check_for_binary_files_in_history():
    import subprocess
    exts = [".exe", ".dll", ".so", ".dylib", ".bin", ".o", ".a"]
    found = []
    out = subprocess.run(["git", "log", "--pretty=format:", "--name-only"], capture_output=True, text=True)
    for line in out.stdout.splitlines():
        if any(line.lower().endswith(e) for e in exts):
            found.append(line)
    return list(set(found))

def check_for_binary_files_in_releases():
    import os
    found = []
    if os.path.exists("dist"):
        for f in os.listdir("dist"):
            if any(f.lower().endswith(e) for e in [".exe", ".dll", ".so", ".dylib", ".bin"]):
                found.append(os.path.join("dist", f))
    return found

def check_for_binary_files_in_assets():
    import os
    found = []
    if os.path.exists("assets"):
        for f in os.listdir("assets"):
            if any(f.lower().endswith(e) for e in [".exe", ".dll", ".so", ".dylib", ".bin"]):
                found.append(os.path.join("assets", f))
    return found

def check_for_binary_files_in_docs():
    import os
    found = []
    if os.path.exists("docs"):
        for root, dirs, files in os.walk("docs"):
            for f in files:
                if any(f.lower().endswith(e) for e in [".exe", ".dll", ".so", ".dylib", ".bin"]):
                    found.append(os.path.join(root, f))
    return found

def check_for_binary_files_in_examples():
    import os
    found = []
    if os.path.exists("examples"):
        for root, dirs, files in os.walk("examples"):
            for f in files:
                if any(f.lower().endswith(e) for e in [".exe", ".dll", ".so", ".dylib", ".bin"]):
                    found.append(os.path.join(root, f))
    return found

def check_for_binary_files_in_tests():
    import os
    found = []
    if os.path.exists("tests"):
        for root, dirs, files in os.walk("tests"):
            for f in files:
                if any(f.lower().endswith(e) for e in [".exe", ".dll", ".so", ".dylib", ".bin"]):
                    found.append(os.path.join(root, f))
    return found

def print_all_binary_artifacts(directory):
    files = find_binary_files(directory)
    for f in files:
        print(f)

