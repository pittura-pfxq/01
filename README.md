# MIS2001 Week 11 - Exercise 1 (CI/CD with GitHub Actions)

A simple Python application with automated testing via GitHub Actions.

## Run Locally

```bash
python app.py
pip install -r requirements.txt
pytest
```

## CI/CD Workflow

Defined in `.github/workflows/ci.yml`:
- **Triggers:** `push` and `pull_request` on `main`, plus manual trigger (`workflow_dispatch`).
- **Actions:** Checks out code, sets up Python 3.11, installs dependencies from `requirements.txt`, compiles `app.py`, and runs `pytest`.
