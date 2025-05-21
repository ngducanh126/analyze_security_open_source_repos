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

def check_for_open_security_groups_tf(tf_file):
    with open(tf_file, "r", encoding="utf-8") as f:
        for line in f:
            if "0.0.0.0/0" in line:
                return True
    return False

def check_for_wildcard_iam_roles_tf(tf_file):
    with open(tf_file, "r", encoding="utf-8") as f:
        for line in f:
            if '"*" in' in line or "'*' in" in line:
                return True
    return False

def check_for_open_security_groups_cfn(cfn_file):
    with open(cfn_file, "r", encoding="utf-8") as f:
        for line in f:
            if "0.0.0.0/0" in line:
                return True
    return False

def check_for_wildcard_iam_roles_cfn(cfn_file):
    with open(cfn_file, "r", encoding="utf-8") as f:
        for line in f:
            if '"*" in' in line or "'*' in" in line:
                return True
    return False

def check_for_open_security_groups_pulumi(pulumi_file):
    with open(pulumi_file, "r", encoding="utf-8") as f:
        for line in f:
            if "0.0.0.0/0" in line:
                return True
    return False

def check_for_wildcard_iam_roles_pulumi(pulumi_file):
    with open(pulumi_file, "r", encoding="utf-8") as f:
        for line in f:
            if '"*"' in line or "'*'" in line:
                return True
    return False

def print_infra_as_code_report(directory):
    print("Terraform files:", find_terraform_files(directory))
    print("CloudFormation files:", find_cloudformation_files(directory))
    print("Pulumi files:", find_pulumi_files(directory))

def check_for_unencrypted_storage_tf(tf_file):
    with open(tf_file, "r", encoding="utf-8") as f:
        for line in f:
            if "unencrypted" in line or "encryption = false" in line:
                return True
    return False

def check_for_unencrypted_storage_cfn(cfn_file):
    with open(cfn_file, "r", encoding="utf-8") as f:
        for line in f:
            if "unencrypted" in line or "Encryption: false" in line:
                return True
    return False

def check_for_unencrypted_storage_pulumi(pulumi_file):
    with open(pulumi_file, "r", encoding="utf-8") as f:
        for line in f:
            if "unencrypted" in line or "encryption=False" in line:
                return True
    return False

