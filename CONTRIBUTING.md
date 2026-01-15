# Contributing

Thank you for your interest in contributing to pre-commit-snippets!

## Conventional Commits

This project uses [Conventional Commits](https://www.conventionalcommits.org/) to automate versioning and changelog generation.

### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | Description | Version Bump |
|------|-------------|--------------|
| `feat` | A new feature | Minor |
| `fix` | A bug fix | Patch |
| `docs` | Documentation only changes | None |
| `style` | Code style changes (formatting, etc.) | None |
| `refactor` | Code changes that neither fix bugs nor add features | None |
| `perf` | Performance improvements | Patch |
| `test` | Adding or updating tests | None |
| `chore` | Maintenance tasks | None |

### Breaking Changes

To indicate a breaking change, add `!` after the type or include `BREAKING CHANGE:` in the footer:

```
feat!: remove support for Python 3.8

BREAKING CHANGE: Python 3.8 is no longer supported.
```

### Examples

```
feat: add support for multiple snippet repositories
fix: handle missing SNIPPET-END marker gracefully
docs: update README with configuration examples
refactor: extract YAML parsing into separate module
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/RemoteRabbit/pre-commit-snippets.git
cd pre-commit-snippets

# Create venv, install dependencies, and set up pre-commit hooks
make setup
```

This will:

1. Create a virtual environment in `.venv/`
2. Install development dependencies (ruff, mypy, pytest, pre-commit)
3. Install pre-commit hooks

Or manually:

```bash
python3 -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
pip install ruff mypy pytest pre-commit
pre-commit install
```

### Project Structure

```
pre-commit-snippets/
├── main.py                      # CLI entry point
├── pre_commit_snippet/
│   ├── __init__.py              # Package init, version
│   ├── cache.py                 # Hash computation and caching
│   ├── cli.py                   # Argument parsing and main orchestration
│   ├── config.py                # YAML parsing, Config/SnippetSource dataclasses
│   ├── git.py                   # Git operations (clone, stage, etc.)
│   ├── logging.py               # Logging configuration
│   └── snippet.py               # Core snippet replacement logic
├── tests/
│   ├── __init__.py
│   └── test_main.py             # Test suite (12 tests)
├── Makefile                     # Development commands
├── pyproject.toml               # Project configuration
└── .github/workflows/           # CI and release automation
```

### Pre-commit Hooks

This project uses pre-commit to run checks before each commit:

- Trailing whitespace removal
- End-of-file fixer
- YAML/JSON validation
- Ruff linting and formatting

To run all hooks manually:

```bash
pre-commit run --all-files
```

### Running Tests

```bash
make test
```

Or manually:

```bash
pytest tests/ -v
```

The test suite covers:

- Snippet replacement in single and multiple files
- Cache file creation and no-rewrite optimization
- Missing snippet warnings
- Missing end marker warnings
- Missing config error handling
- Empty target files handling
- Dry-run mode
- Verbose and debug output
- Branch/tag configuration

### Testing Locally

To test the hook locally:

1. **Create a test snippet repository** with some `.md` files:

   ```bash
   mkdir /tmp/test-snippets
   cd /tmp/test-snippets
   git init
   echo "This is a test snippet." > greeting.md
   git add . && git commit -m "Add test snippet"
   ```

2. **Create a test target repository** with a config and markdown file:

   ```bash
   mkdir /tmp/test-repo
   cd /tmp/test-repo
   git init

   # Create config
   cat > .pre-commit-snippets-config.yaml << EOF
   snippet_repo: /tmp/test-snippets
   target_files:
     - README.md
   EOF

   # Create a markdown file with snippet markers
   cat > README.md << EOF
   # Test

   <!-- SNIPPET-START: greeting -->
   placeholder
   <!-- SNIPPET-END -->
   EOF

   git add . && git commit -m "Initial commit"
   ```

3. **Run the hook**:

   ```bash
   cd /tmp/test-repo
   python /path/to/pre-commit-snippets/main.py --verbose
   ```

4. **Verify** the README.md was updated with the snippet content.

### Debugging

Use the `--debug` flag to see detailed logging:

```bash
python main.py --debug
```

This shows:
- Commands being executed
- File paths being processed
- Hash values for cache comparisons
- Cache load/save operations

### Linting

```bash
make check  # Run all checks (lint, format, typecheck, test)

# Or individual commands:
make lint       # Run ruff linter
make format     # Format code
make typecheck  # Run mypy
```

### Available Make Commands

```bash
make help  # Show all available commands
```

| Command | Description |
|---------|-------------|
| `make venv` | Create virtual environment |
| `make install` | Install dev dependencies |
| `make install-docs` | Install docs dependencies |
| `make install-all` | Install all dependencies |
| `make setup` | Install deps and set up pre-commit hooks |
| `make lint` | Run ruff linter |
| `make format` | Format code with ruff |
| `make typecheck` | Run mypy type checker |
| `make test` | Run tests |
| `make check` | Run all checks |
| `make docs-serve` | Serve docs locally |
| `make docs-build` | Build docs |
| `make clean` | Remove generated files |

## Releases

Releases are automated using [Release Please](https://github.com/googleapis/release-please). When commits following the Conventional Commits format are merged to `main`, Release Please will:

1. Create/update a release PR with changelog updates
2. When the release PR is merged, create a GitHub release with the appropriate version tag
