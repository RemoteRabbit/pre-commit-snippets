.PHONY: help venv install install-docs setup lint format format-check typecheck test check docs-serve docs-build clean

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

venv: $(VENV)/bin/activate ## Create virtual environment

install: venv ## Install development dependencies
	$(PIP) install ruff mypy pytest pre-commit

install-docs: venv ## Install documentation dependencies
	$(PIP) install -e ".[docs]"

install-all: install install-docs ## Install all dependencies

setup: install ## Install deps and set up pre-commit hooks
	$(VENV)/bin/pre-commit install

lint: venv ## Run ruff linter
	$(VENV)/bin/ruff check .

format: venv ## Format code with ruff
	$(VENV)/bin/ruff format .

format-check: venv ## Check code formatting without changes
	$(VENV)/bin/ruff format --check .

typecheck: venv ## Run mypy type checker
	$(VENV)/bin/mypy main.py pre_commit_snippet/ --ignore-missing-imports

test: venv ## Run tests
	$(VENV)/bin/pytest tests/ -v

check: lint format-check typecheck test ## Run all checks (lint, format, typecheck, test)

docs-serve: install-docs ## Serve documentation locally
	$(VENV)/bin/mkdocs serve

docs-build: install-docs ## Build documentation
	$(VENV)/bin/mkdocs build --strict

clean: ## Remove generated files
	rm -rf $(VENV) __pycache__ .pytest_cache .mypy_cache site/ *.pyc
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
