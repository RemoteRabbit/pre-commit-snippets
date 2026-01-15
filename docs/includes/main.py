"""
MkDocs Macros plugin main module.

Define custom macros and filters for use in documentation.
"""


def define_env(env):
    """Define custom macros and variables for MkDocs."""

    # Project metadata
    env.variables["project_name"] = "pre-commit-snippet"
    env.variables["min_python_version"] = "3.9"

    @env.macro
    def since(version: str) -> str:
        """Generate a 'since version' badge."""
        return f'<span class="md-tag">since v{version}</span>'

    @env.macro
    def deprecated(version: str, alternative: str = "") -> str:
        """Generate a deprecation notice."""
        msg = f"Deprecated since v{version}."
        if alternative:
            msg += f" Use `{alternative}` instead."
        return f'!!! warning "Deprecated"\n    {msg}'

    @env.macro
    def feature_flag(name: str) -> str:
        """Generate a feature flag notice."""
        return f'!!! info "Feature Flag"\n    This feature requires the `{name}` flag to be enabled.'

    @env.macro
    def cli_command(command: str, description: str) -> str:
        """Generate formatted CLI command documentation."""
        return f"""
```bash
{command}
```

{description}
"""

    @env.macro
    def config_option(name: str, type_: str, default: str, description: str) -> str:
        """Generate formatted configuration option documentation."""
        return f"""
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `{name}` | `{type_}` | `{default}` | {description} |
"""
