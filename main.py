#!/usr/bin/env python3
"""
Pre-commit hook that expands markdown snippets using paired start/end markers.

This is the entry point for the pre-commit hook. The actual implementation
is in the pre_commit_snippet package.
"""

import sys

from pre_commit_snippet.cli import main

if __name__ == "__main__":
    sys.exit(main())
