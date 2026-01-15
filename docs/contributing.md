# Contributing

Thank you for your interest in contributing to pre-commit-snippet!

## Development Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/pre-commit-snippet.git
cd pre-commit-snippet

# Install dependencies and set up pre-commit hooks
make setup
```

## Running Tests

```bash
make test
```

## Running All Checks

```bash
make check  # lint, format, typecheck, test
```

## Building Documentation

```bash
# Install docs dependencies
pip install mkdocs mkdocs-material mkdocstrings[python]

# Serve locally
make docs-serve

# Build static site
make docs-build
```

## Conventional Commits

This project uses [Conventional Commits](https://www.conventionalcommits.org/) for automated versioning.

### Commit Types

| Type | Description | Version Bump |
|------|-------------|--------------|
| `feat` | A new feature | Minor |
| `fix` | A bug fix | Patch |
| `docs` | Documentation only | None |
| `refactor` | Code refactoring | None |
| `test` | Adding tests | None |
| `chore` | Maintenance | None |

### Examples

```
feat: add support for multiple snippet repositories
fix: handle missing SNIPPET-END marker gracefully
docs: update README with configuration examples
```

## Release Process

Releases are automated using [Release Please](https://github.com/googleapis/release-please).

1. Merge commits following Conventional Commits format
2. Release Please creates/updates a release PR
3. Merge the release PR to create a GitHub release
