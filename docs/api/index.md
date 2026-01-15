# API Reference

This section documents the Python API for pre-commit-snippet.

## Package Structure

```
pre_commit_snippet/
├── __init__.py     # Package init, exports main()
├── cache.py        # Hash computation and caching
├── cli.py          # Command-line interface
├── config.py       # Configuration loading
├── git.py          # Git operations
├── logging.py      # Logging configuration
└── snippet.py      # Snippet replacement logic
```

## Modules

| Module | Description |
|--------|-------------|
| [cli](cli.md) | Main entry point and argument parsing |
| [config](config.md) | Configuration loading and validation |
| [cache](cache.md) | Hash computation and cache management |
| [git](git.md) | Git operations (clone, stage, etc.) |
| [snippet](snippet.md) | Core snippet replacement logic |
| [logging](logging.md) | Logging configuration |

## Quick Example

```python
from pre_commit_snippet import main

# Run with default arguments
exit_code = main()
```
