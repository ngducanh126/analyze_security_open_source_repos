def parse_requirements(requirements_file):
    with open(requirements_file, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    pkgs = {}
    for line in lines:
        if "==" in line:
            pkg, ver = line.split("==")
            pkgs[pkg.strip()] = ver.strip()
    return pkgs

