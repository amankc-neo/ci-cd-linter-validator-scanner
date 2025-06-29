import sys
import yaml
import os
from scanner.utils import find_yaml_files, load_yaml
from scanner.opa_runner import evaluate_with_opa

REQUIRED_KEYS = ['jobs']
BLOCKED_PATTERNS = ['latest', 'set-env', 'add-path']

def lint_yaml(file_path):
    errors = []

    try:
        data = load_yaml(file_path)

        # Check if 'jobs' exists
        if not any(key in data for key in REQUIRED_KEYS):
            errors.append(f"[ERROR] Missing required key(s): {REQUIRED_KEYS}")

        yaml_str = yaml.dump(data)

        # Check for blocked patterns
        for pattern in BLOCKED_PATTERNS:
            if pattern in yaml_str:
                errors.append(f"[ERROR] Usage of forbidden pattern: '{pattern}'")

        # Check for permissions
        if 'permissions' not in yaml_str:
            errors.append(f"[WARNING] 'permissions:' block not found")

    except Exception as e:
        errors.append(f"[FATAL] Failed to parse {file_path}: {str(e)}")

    return errors, data

def main(file_path):
    print(f"🔍 Linting: {file_path}")
    errors, parsed_yaml = lint_yaml(file_path)

    if errors:
        for err in errors:
            print(err)
    else:
        print("✅ Lint passed")

    # Pass to OPA
    print("\n🛡️ Running OPA policies...")
    opa_results = evaluate_with_opa(parsed_yaml)

    if opa_results:
        for result in opa_results:
            print(f"[OPA POLICY] {result}")
    else:
        print("✅ OPA policy check passed")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python linter.py <path-to-yaml>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    if not os.path.isfile(yaml_file):
        print(f"File not found: {yaml_file}")
        sys.exit(1)

    main(yaml_file)
