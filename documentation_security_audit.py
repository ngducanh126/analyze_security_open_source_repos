def check_security_section_in_readme(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return "security" in content

def check_responsible_disclosure_instructions(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return "disclosure" in content or "report a vulnerability" in content

def check_contact_email_in_docs(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read()
        import re
        return bool(re.search(r"[\w\.-]+@[\w\.-]+", content))

def check_security_policy_file():
    return os.path.exists("SECURITY.md")

