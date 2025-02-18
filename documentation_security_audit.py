def check_security_section_in_readme(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return "security" in content

