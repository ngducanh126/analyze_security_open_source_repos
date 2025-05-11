def find_terraform_files(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".tf"):
                found.append(os.path.join(root, f))
    return found

def find_cloudformation_files(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".yaml") or f.endswith(".yml") or f.endswith(".json"):
                if "cloudformation" in f.lower():
                    found.append(os.path.join(root, f))
    return found

def find_pulumi_files(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".ts") or f.endswith(".py") or f.endswith(".go"):
                if "pulumi" in f.lower():
                    found.append(os.path.join(root, f))
    return found

