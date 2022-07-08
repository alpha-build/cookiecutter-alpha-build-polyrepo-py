# Cookiecutter Template for Polyrepo Project powered by AlphaBuild

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

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
cookiecutter https://github.com/alpha-build/cookiecutter-alpha-build-polyrepo-py
```

Please answer to the questions when prompted. Finally, `cd` into the newly created project.
Next, check `CONTRIBUTING.md` to set up the development environment. In short, the steps will look like:

```bash
cd <your-project>
# Create and activate the environment, e.g. with conda
conda create -n my-env python=3.9 -y
conda activate my-env
# Test if "reproducing" the environment works (i.e. get all the packages with the versions according to the lock file).
# In CI and most developers will use this command to make sure the dependencies they are using are exactly the same as
# as everyone else's. This reproducibility is achieved thanks to a file `3rdparty/constraints.txt`, called "lock file".
make env
# To upgrade / modify the environment, one needs to change the lock file. If one wants to add or remove packages from
# the environment one should edit `3rdparty/requirements.txt` (for core dependencies) or `3rdparty/requirements-dev.txt`
# (for dev-only dependencies) and then regenerate the lock file. Because the lock file associated with the project may
# become outdated, let's also run the upgrade.
make env-upgrade
# Set up as a git repo
git init
git add .
# The `cookiecutter` template uses "floating" the versions which is not reproducible but it is left this way such that
# users can get the latest versions of the linters / formatters when they get started with the project
pre-commit autoupdate
# Let's test whether linting works
make lint  # Run twice if the first run didn't succeed (the auto-formatters in the first run should have fixed the issues)
# Let's test whether testing works
make test
# To test whether everything works with multiple Python versions, run the same tests but with "nox".
nox -db conda  # To create the environments with conda
# Or without conda (provided you have multiple python versions already installed)
nox
```

If you are on Windows and don't have make installed, please check the `CONTRIBUTING.md` to set it up.

**You are all set up now. Happy Coding!**
