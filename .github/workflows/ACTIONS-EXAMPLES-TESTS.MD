### Add and run the below workflows to test and play with actions

---
```yaml
  test:
    runs-on: ubuntu-latest
    name: Run Unit + Policy Tests
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install pytest
        run: pip install -r requirements.txt pytest

      - name: Run Python unit tests
        run: pytest tests/

      - name: Install OPA
        run: |
          curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64
          chmod +x opa && sudo mv opa /usr/local/bin

      - name: Run Rego policy tests
        run: opa test policies/base/
```
---

```yaml
name: CI/CD YAML Validator & Policy Tester

on:
  pull_request:
    paths:
      - '**.yml'
      - '**.yaml'
      - 'scanner/**'
      - 'policies/**'
      - 'tests/**'

jobs:
  validate-yamls:
    runs-on: ubuntu-latest
    name: Lint & Validate YAMLs (Non-blocking)
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Python dependencies
        run: pip install -r requirements.txt

      - name: Install OPA CLI
        run: |
          curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64
          chmod +x opa && sudo mv opa /usr/local/bin

      - name: Run YAML Linter (Non-blocking)
        run: |
          echo " Validating bad_workflow.yml"
          python scanner/linter.py examples/bad_workflow.yml || true

  test:
    runs-on: ubuntu-latest
    name: Unit Tests & Policy Checks (Non-blocking)
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install test dependencies
        run: pip install -r requirements.txt pytest

      - name: Run Python unit tests (Non-blocking)
        run: pytest tests/ || true

      - name: Install OPA
        run: |
          curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64
          chmod +x opa && sudo mv opa /usr/local/bin

      - name: Run Rego policy tests (Non-blocking)
        run: opa test policies/base/ || true
```
---

```yaml
name: "CI/CD YAML Linter and Policy Scanner"
description: "Validates GitHub Actions workflows using Python linter and OPA policies"
author: "Aman Choudhary"

inputs:
  target_file:
    description: "Path to the YAML file to validate"
    required: true
  strict_mode:
    description: "Enable strict rule set (policies/strict/)"
    required: false
    default: "false"

runs:
  using: "composite"
  steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install Python dependencies
      run: pip install -r requirements.txt
      shell: bash

    - name: Install OPA CLI
      run: |
        curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64
        chmod +x opa && sudo mv opa /usr/local/bin/
      shell: bash

    - name: Run validator
      run: |
        echo "🔍 Validating ${{ inputs.target_file }}"
        python scanner/linter.py ${{ inputs.target_file }}
      shell: bash
```
---
