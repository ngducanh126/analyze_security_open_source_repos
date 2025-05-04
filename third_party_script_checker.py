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

def find_css_without_sri(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<link" in line and "href=" in line and "stylesheet" in line and "integrity=" not in line:
                            found.append((path, i+1, line.strip()))
    return found

def find_external_scripts_in_js(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".js"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "http" in line and ".js" in line:
                            found.append((path, i+1, line.strip()))
    return found

def find_external_scripts_in_markdown(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<script" in line and "src=" in line:
                            found.append((path, i+1, line.strip()))
    return found

def find_external_scripts_in_notebooks(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".ipynb"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<script" in line and "src=" in line:
                            found.append((path, i+1, line.strip()))
    return found

def find_external_scripts_in_templates(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".j2") or f.endswith(".jinja2"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<script" in line and "src=" in line:
                            found.append((path, i+1, line.strip()))
    return found

def print_external_script_report(directory):
    print("HTML scripts:", find_external_scripts_in_html(directory))
    print("Scripts without SRI:", find_scripts_without_sri(directory))
    print("External CSS:", find_external_css_in_html(directory))
    print("CSS without SRI:", find_css_without_sri(directory))
    print("External JS in JS files:", find_external_scripts_in_js(directory))
    print("External scripts in markdown:", find_external_scripts_in_markdown(directory))
    print("External scripts in notebooks:", find_external_scripts_in_notebooks(directory))
    print("External scripts in templates:", find_external_scripts_in_templates(directory))

def find_external_scripts_in_yaml(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".yml") or f.endswith(".yaml"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<script" in line and "src=" in line:
                            found.append((path, i+1, line.strip()))
    return found

def find_external_scripts_in_config(directory):
    import os
    found = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".conf") or f.endswith(".ini"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    for i, line in enumerate(file):
                        if "<script" in line and "src=" in line:
                            found.append((path, i+1, line.strip()))
    return found

