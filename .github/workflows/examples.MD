### Add and run the below workflows to test and play with actions

---
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

---
