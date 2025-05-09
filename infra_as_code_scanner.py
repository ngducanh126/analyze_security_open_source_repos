def find_terraform_files(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".tf"):
                found.append(os.path.join(root, f))
    return found

