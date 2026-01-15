# Installation

**Current version: {{ version }}**

## Using pre-commit framework

The recommended way to use pre-commit-snippet is with the [pre-commit](https://pre-commit.com/) framework.

Add this to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/YOUR_USERNAME/pre-commit-snippet
    rev: v0.1.0  # Use the latest tag
    hooks:
      - id: snippet-sync
```

Then install the hooks:

```bash
pre-commit install
```

## Using pip

Install directly with pip:

```bash
pip install pre-commit-snippet
```

Then run manually or add to your workflow:

```bash
pre-commit-snippet
```

## Manual installation

Clone the repository and run directly:

```bash
git clone https://github.com/YOUR_USERNAME/pre-commit-snippet.git
cd pre-commit-snippet
python main.py
```

## Requirements

- Python 3.9 or higher
- Git (for cloning snippet repositories)
