# CI/CD Linter, Validator, and Security Scanner

> **Tech Stack**: Python • OPA • Rego • GitHub Actions  
> **Goal**: Ensure secure, standardized, and best-practice-compliant CI/CD pipeline definitions through automated static analysis and policy enforcement.

---

## 🔍 Overview

This tool acts as a pre-merge gatekeeper for CI/CD pipeline definitions (like GitHub Actions), ensuring:

- YAML linting and schema checks
- Enforcement of best practices (e.g., no `latest` tags, job isolation)
- Security policy checks using Open Policy Agent (OPA) + Rego
- Seamless GitHub Action integration for PR validation

---

## 📁 Repository Structure

![image](https://github.com/user-attachments/assets/cddb8a63-6c4a-4c87-85ca-7b6056ea52b7)



**Repo Breakdown:**

- `scanner/`: Python CLI for YAML linting and OPA policy evaluation.
- `policies/`: Rego rules for CI/CD security and best practices.
- `examples/`: Sample GitHub Action YAMLs showing good and bad patterns.
- `.github/workflows/`: CI pipeline that runs the scanner on PRs.
- `tests/`: Unit tests for linter and policy engine.
- `action.yml`: Optional reusable GitHub Action.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.
- `LICENSE`: License file.

---

## ⚙️ Features

- 🔒 Rego-based policy enforcement (OPA)
- ✅ Linter for common YAML anti-patterns
- 🔧 Easily extensible with custom rules
- 🚦 GitHub Actions workflow for automated validation on PRs
- 📊 Examples of good and bad CI/CD definitions

---

### Clone the repo
```bash
git clone https://github.com/yourusername/ci-cd-linter-validator-scanner.git
cd ci-cd-linter-validator-scanner
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run locally
```bash
python scanner/linter.py examples/bad_workflow.yml
```
---

## Policy Design

- All policies are defined in Rego and organized in:

- policies/base/: Core rules (secure-by-default)

- policies/strict/: Stricter org-level rules

- policies/custom/: User-defined rules

- See Policy Writing Guide for more.

---

## 🛠 GitHub Actions Integration

- The GitHub Action is defined in .github/workflows/validate.yml.
- It automatically validates every PR containing pipeline YAMLs.

You can reuse the action with:

- uses: your-org/ci-cd-linter-validator-scanner@main

---

## 📄 Example Rules

- Deny latest tag usage
- Require permissions: field in workflows
- Block use of add-path / set-env
- Require checkout@v3 or above
- Good vs Bad

---

## 🧩 Extending
- Want to write your own rules? Just drop a new .rego file in policies/custom/ and you’re good to go.

---

## Terms of Use

- This repository is open for educational and reference purposes.  
- You are free to explore, copy, and adapt the ideas and structure.  
- No warranty or support is provided.

---

