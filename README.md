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

ci-cd-linter-validator-scanner/
├── scanner/ # Core Python CLI logic (linting + OPA execution)
│ ├── init.py
│ ├── linter.py # YAML anti-pattern checker
│ ├── opa_runner.py # Runs OPA with Rego policies
│ └── utils.py # Common utilities
│
├── policies/ # OPA policy files (Rego)
│ ├── base/ # General rules
│ ├── strict/ # Optional strict rules
│ └── custom/ # Placeholder for org/team rules
│
├── examples/ # Good vs bad workflow examples
│ ├── good_workflow.yml
│ └── bad_workflow.yml
│
├── .github/
│ └── workflows/
│ └── validate.yml # GitHub Action to run the linter+validator
│
├── tests/ # Unit and integration tests
│ ├── test_linter.py
│ └── test_opa_runner.py
│
├── action.yml # (Optional) GitHub Reusable Action definition
├── requirements.txt # Python dependencies
├── README.md # Project overview and usage
└── LICENSE

**Legend:**

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
