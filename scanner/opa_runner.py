# scanner/opa_runner.py

import json
import subprocess
import os
import tempfile

OPA_POLICY_DIR = "policies/base"

def evaluate_with_opa(yaml_data):
    violations = []

    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp_input:
        json.dump(yaml_data, tmp_input)
        tmp_input.flush()

        try:
            result = subprocess.run([
                "opa", "eval",
                "--format", "json",
                "--data", OPA_POLICY_DIR,
                "--input", tmp_input.name,
                "data"
            ], capture_output=True, text=True, check=True)

            output = json.loads(result.stdout)
            for result_set in output.get("result", []):
                for expression in result_set.get("expressions", []):
                    value = expression.get("value")
                    if isinstance(value, list):
                        violations.extend(value)

        except subprocess.CalledProcessError as e:
            violations.append(f"[OPA ERROR] {e.stderr.strip()}")

        finally:
            os.remove(tmp_input.name)

    return violations
