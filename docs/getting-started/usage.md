# Usage

## Snippet Markers

Add markers to your markdown files to indicate where snippets should be inserted:

```markdown
# My Project

<!-- SNIPPET-START: license-notice -->
This content will be replaced with the contents of `license-notice.md` from your snippet repo.
<!-- SNIPPET-END -->

## Other content...
```

The snippet name (`license-notice` in this example) corresponds to a file in your snippet repository (`license-notice.md`).

## Command Line Options

```bash
pre-commit-snippet [OPTIONS]
```

### `--dry-run`

Preview changes without modifying files.

```bash
pre-commit-snippet --dry-run
```

### `--verbose`, `-v`

Print info-level logs showing files being processed and updates.

```bash
pre-commit-snippet --verbose
```

### `--debug`

Print debug-level logs with timestamps, commands, and hash values.

```bash
pre-commit-snippet --debug
```

## Examples

### Normal Run

```bash
$ pre-commit-snippet
```

No output if all snippets are up to date.

### Preview Changes

```bash
$ pre-commit-snippet --dry-run
Would update: README.md
Dry run complete. No files were modified.
```

### Verbose Output

```bash
$ pre-commit-snippet --verbose
Snippet repo: https://github.com/your-org/snippets.git
Target files: README.md, CONTRIBUTING.md
Processing README.md
Updating snippet 'license-notice' in README.md
Processing CONTRIBUTING.md
All snippets are up to date
Staged modified files
```

### Debug Output

```bash
$ pre-commit-snippet --debug
2024-01-15 10:30:00 [DEBUG] pre_commit_snippet: Starting pre-commit-snippet
2024-01-15 10:30:00 [DEBUG] pre_commit_snippet: Running command: git rev-parse --show-toplevel
2024-01-15 10:30:00 [DEBUG] pre_commit_snippet: Repository root: /home/user/project
...
```

## How It Works

1. **Clone**: Shallow clones the snippet repository to a temporary directory
2. **Parse**: Finds all `SNIPPET-START` / `SNIPPET-END` marker pairs in target files
3. **Compare**: Computes SHA-256 hashes to detect changes
4. **Replace**: Updates blocks only when the snippet has changed
5. **Cache**: Saves hashes to avoid recomputing on the next run
6. **Stage**: Automatically stages modified files for commit
7. **Cleanup**: Removes the temporary clone
