def find_external_scripts_in_html(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<script" in line and "src=" in line:
                            found.append((path, i+1, line.strip()))
    return found

def find_scripts_without_sri(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<script" in line and "src=" in line and "integrity=" not in line:
                            found.append((path, i+1, line.strip()))
    return found

def find_external_css_in_html(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<link" in line and "href=" in line and "stylesheet" in line:
                            found.append((path, i+1, line.strip()))
    return found

