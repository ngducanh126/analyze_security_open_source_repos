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

def check_security_badge_in_readme(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return "badge" in content and "security" in content

def check_for_changelog():
    return os.path.exists("CHANGELOG.md")

def check_for_code_of_conduct():
    return os.path.exists("CODE_OF_CONDUCT.md")

def check_for_contributing_guide():
    return os.path.exists("CONTRIBUTING.md")

def check_for_security_labels_in_issues():
    import requests
    url = "https://api.github.com/repos/owner/repo/labels"
    resp = requests.get(url)
    if resp.status_code == 200:
        return any("security" in l["name"].lower() for l in resp.json())
    return False

def check_for_security_faq():
    return os.path.exists("SECURITY_FAQ.md")

def check_for_security_examples(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return "example" in content and "security" in content

def check_for_security_toc(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read().lower()
        return "table of contents" in content and "security" in content

def check_for_security_glossary():
    return os.path.exists("SECURITY_GLOSSARY.md")

def check_for_security_architecture_docs():
    return os.path.exists("SECURITY_ARCHITECTURE.md")

def check_for_security_training_docs():
    return os.path.exists("SECURITY_TRAINING.md")

def check_for_security_incident_response():
    return os.path.exists("SECURITY_INCIDENT_RESPONSE.md")

