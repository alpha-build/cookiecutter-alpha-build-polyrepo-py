# Cookiecutter Template for Polyrepo Project powered by AlphaBuild

This is a template for generic Python projects. The aim is to automate as much as possible while ensuring high
standards are met. For this, users of this template can take advantage of:

- _Lots_ of linters (for more than Python) and code auto-formatters configured such that they don't conflict
  with each other. Please check the `.pre-commit-config.yaml` file to see what tools are being run (most of these tools
  are configured via `pyproject.toml` or specific config files such as `mypy.ini`).
- A fully equipped Python testing framework (including `nox`).
- A framework to easily reproduce / upgrade third party dependencies.
- All the set-up to easily package the app.
- Continuous Integration and CODEOWNERS.

## Getting started

Please `pip install cookiecutter` if you haven't done so already and then run the line below in a terminal.

```bash
cookiecutter https://github.com/cristianmatache/cookiecutter-alpha-build-polyrepo-py
```

Please answer to the questions when prompted. Finally, `cd` into the newly created project.
Next, check `CONTRIBUTING.md` to set up the development environment.
