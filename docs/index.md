# pre-commit-snippet

A pre-commit hook that automatically syncs markdown snippets from a central repository into your documentation files.

## Features

- **Marker-based replacement**: Uses `<!-- SNIPPET-START: name -->` / `<!-- SNIPPET-END -->` markers to identify replaceable blocks
- **SHA-256 caching**: Only rewrites blocks when the central snippet has actually changed, avoiding unnecessary file churn
- **Automatic staging**: Modified files are automatically staged for commit
- **Branch/tag support**: Pin snippets to a specific branch or tag
- **Dry-run mode**: Preview changes without modifying files
- **Debug logging**: Detailed logging for troubleshooting

## Quick Start

```bash
pip install pre-commit-snippet
```

Create a `pre-commit-snippet-config.yaml`:

```yaml
snippet_repo: https://github.com/your-org/snippets.git
target_files:
  - README.md
```

Add markers to your markdown files:

```markdown
<!-- SNIPPET-START: my-snippet -->
This will be replaced with content from my-snippet.md
<!-- SNIPPET-END -->
```

Run the hook:

```bash
pre-commit-snippet
```

## Next Steps

- [Installation](getting-started/installation.md) - Detailed installation options
- [Configuration](getting-started/configuration.md) - All configuration options
- [Usage](getting-started/usage.md) - Command line options and examples
- [API Reference](api/index.md) - Module documentation
