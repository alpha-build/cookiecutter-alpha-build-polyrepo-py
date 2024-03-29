# Cookiecutter Template for Polyrepo Project powered by AlphaBuild

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

This is a template for generic Python projects. The aim is to automate as much as possible while ensuring high
standards are met. For this, users of this template can take advantage of:

- _Lots_ of linters (for more than Python) and code auto-formatters configured such that they don't conflict
  with each other. Please check the `.pre-commit-config.yaml` file to see what tools are being run (most of these tools
  are configured via `pyproject.toml` or specific config files such as `mypy.ini`).
- A fully equipped Python testing framework (including `nox`).
- A framework to easily reproduce / upgrade third party dependencies.
- All the set-up to easily package and auto-version the project.
- Continuous Integration and `CODEOWNERS` (these features are only implemented for Github,
  while the others are general).

## Getting started

Please `pip install cookiecutter` if you haven't done so already and then run the line below in a terminal.

```bash
cookiecutter https://github.com/alpha-build/cookiecutter-alpha-build-polyrepo-py
```

Please answer to the questions when prompted. Finally, `cd` into the newly created project.
Next, check `CONTRIBUTING.md` to set up the development environment. In short, the steps will look like:

## One-off set-up after creating the project

```bash
cd <your-project>
```

Create and activate the environment, e.g. with conda

```bash
conda create -n my-env python=3.10 -y
conda activate my-env
```

Test if "reproducing" the environment works (i.e. get all the packages with the versions according to the lock file).
The CI pipeline and most developers will use this command to make sure the dependencies they are using are exactly the
same as everyone else's. This reproducibility is achieved thanks to a file `3rdparty/constraints.txt`,
called "lock file".

To upgrade or modify the environment, one needs to change the lock file. If one wants to add or remove packages from
the environment one should edit `3rdparty/requirements.txt` (for core dependencies) or `3rdparty/requirements-dev.txt`
(for dev-only dependencies) and then regenerate the lock file. Because the lock file associated with the project may
become outdated, let's also run the environment upgrade.

```bash
make env  # Reproduce according to the lock file
make env-upgrade  # Upgrade the environment and the lock file
```

Set up as a git repo

```bash
git init
git add .
```

The `cookiecutter` template uses "floating" the versions which is not reproducible but it is left this way such that
users can get the latest versions of the linters / formatters when they get started with the project

```bash
pre-commit autoupdate
```

Let's test whether linting works. Run twice if the first run didn't succeed (the auto-formatters in the first run should
have fixed the issues).

```bash
make lint
```

If you haven't set up make on your machine, you can try running `pre-commit run --all-files`.
Let's test whether testing works as well.

```bash
make test
```

Again, if you haven't set up make on your machine, you can try running `pytest --rootdir=. -m "" -k ""tests/`.
To test whether everything works with multiple Python versions, run the same tests but with "nox".

```bash
nox -db conda  # To create the environments with conda
# Or without conda (provided you have multiple python versions already installed)
nox
```

If you are on Windows and don't have make installed, please check the `CONTRIBUTING.md` to set it up.

**You are all set up now. Happy Coding!**
