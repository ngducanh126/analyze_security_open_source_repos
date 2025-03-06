def parse_requirements(requirements_file):
    with open(requirements_file, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    pkgs = {}
    for line in lines:
        if "==" in line:
            pkg, ver = line.split("==")
            pkgs[pkg.strip()] = ver.strip()
    return pkgs

def parse_setup_py(setup_file):
    with open(setup_file, "r", encoding="utf-8") as f:
        content = f.read()
    import re
    pkgs = {}
    for match in re.findall(r"['"]([\w\-]+)['"]\s*==\s*['"]([\w\.]+)['"]", content):
        pkgs[match[0]] = match[1]
    return pkgs

