# Configuration

Create a `pre-commit-snippet-config.yaml` file in your repository root.

## Example Configuration

```yaml
# URL of the repository containing your snippets (required)
snippet_repo: https://github.com/your-org/snippets.git

# Branch or tag to use (optional, default: default branch)
snippet_branch: main

# Subdirectory within the snippet repo where snippets are stored (optional)
snippet_subdir: snippets

# File extension for snippet files (optional, default: .md)
snippet_ext: .md

# List of files to process (required)
target_files:
  - README.md
  - docs/CONTRIBUTING.md
  - docs/SECURITY.md
```

## Configuration Options

### `snippet_repo` (required)

URL or path to the repository containing your snippet files.

```yaml
# HTTPS URL
snippet_repo: https://github.com/your-org/snippets.git

# SSH URL
snippet_repo: git@github.com:your-org/snippets.git

# Local path
snippet_repo: /path/to/local/snippets
```

### `snippet_branch` (optional)

Branch or tag to clone from the snippet repository.

```yaml
snippet_branch: main
snippet_branch: v1.0.0
snippet_branch: release/2.0
```

If not specified, the repository's default branch is used.

### `snippet_subdir` (optional)

Subdirectory within the snippet repository where snippet files are located.

```yaml
snippet_subdir: snippets
snippet_subdir: docs/shared
```

Default: `.` (repository root)

### `snippet_ext` (optional)

File extension for snippet files.

```yaml
snippet_ext: .md
snippet_ext: .txt
snippet_ext: .html
```

Default: `.md`

### `target_files` (required)

List of files in your repository to process for snippet markers.

```yaml
target_files:
  - README.md
  - docs/index.md
  - CONTRIBUTING.md
```

Paths are relative to the repository root.

## Cache File

The hook creates a `.snippet-hashes.json` file to track which snippets have been applied.

!!! tip
    Commit this file to your repository to avoid unnecessary rewrites on other machines.
