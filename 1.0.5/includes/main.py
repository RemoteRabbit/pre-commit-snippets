"""
MkDocs Macros plugin main module.

Define custom macros and filters for use in documentation.
"""

from pathlib import Path

import tomllib


def _get_version() -> str:
    """Read version from pyproject.toml."""
    pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    return data["project"]["version"]


def define_env(env):
    """Define custom macros and variables for MkDocs."""

    # Project metadata
    env.variables["project_name"] = "pre-commit-snippet"
    env.variables["min_python_version"] = "3.9"
    env.variables["version"] = _get_version()

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
        return f'!!! info "Feature Flag"\n    Requires the `{name}` flag to be enabled.'

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
