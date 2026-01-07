# Automate

A small **toy Python project** created to practice:
- Python unit testing using `unittest`
- Basic Python project structure
- Continuous Integration (CI) with GitHub Actions

The project implements a simple **Calculator** and automatically runs unit tests on every push and pull request.

---

## Features

- Addition, subtraction, multiplication, and division
- Unit tests using Python’s built-in `unittest` framework
- Automated CI pipeline using GitHub Actions

---

## Project Structure

```
automate/
├── calculator/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
└── .github/workflows/
    └── python-ci.yml
```

---

## Requirements

- Python 3.8 or higher

No external dependencies are required.

---

## Run Tests Locally

From the project root directory:

```bash
python -m unittest discover
```

Verbose output:

```bash
python -m unittest discover -v
```

---

## Continuous Integration

This repository uses **GitHub Actions** to automatically run unit tests on:
- Every push
- Every pull request

The CI pipeline fails if any test fails.

---

### Tagging the release

```bash
git tag v0.1.0
git push origin v0.1.0

```

## Notes

This is a **learning and experimentation project** intended for hands-on practice with Python testing and CI/CD concepts.
