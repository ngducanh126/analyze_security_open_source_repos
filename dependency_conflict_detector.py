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

def parse_pipfile(pipfile):
    with open(pipfile, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    pkgs = {}
    for line in lines:
        if "=" in line and '"' in line:
            pkg, ver = line.split("=")
            pkgs[pkg.strip()] = ver.strip().replace('"','').replace("'",'')
    return pkgs

def find_conflicts(*dicts):
    from collections import defaultdict
    versions = defaultdict(set)
    for d in dicts:
        for pkg, ver in d.items():
            versions[pkg].add(ver)
    return {pkg: list(vers) for pkg, vers in versions.items() if len(vers) > 1}

def check_requirements_vs_setup(requirements_file, setup_file):
    reqs = parse_requirements(requirements_file)
    setup = parse_setup_py(setup_file)
    return find_conflicts(reqs, setup)

def check_requirements_vs_pipfile(requirements_file, pipfile):
    reqs = parse_requirements(requirements_file)
    pip = parse_pipfile(pipfile)
    return find_conflicts(reqs, pip)

def check_setup_vs_pipfile(setup_file, pipfile):
    setup = parse_setup_py(setup_file)
    pip = parse_pipfile(pipfile)
    return find_conflicts(setup, pip)

