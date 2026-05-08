# test-repo

Small Python sample project used to test GitHub PR/CI + Codecov.

## What’s inside

- `app.py`: basic arithmetic helpers: `add`, `subtract`, `multiply`, `divide`
- `test_app.py`: `pytest` tests (intentionally skips `multiply` to demonstrate uncovered code)
- GitHub Actions workflow runs tests with coverage and uploads to Codecov

## Requirements

- Python 3.10+ (CI uses Python 3.10)

## Setup

Create and activate a virtual environment (optional but recommended), then install dependencies:

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```

## Run tests with coverage (like CI)

```bash
pytest --cov=./ --cov-report=xml
```

