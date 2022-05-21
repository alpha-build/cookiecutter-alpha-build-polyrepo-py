# Contributing guidelines

1. [Frequent actions](#frequent-actions)
2. [Initial set-up](#initial-set-up)
   1. [Build system](#build-system)
   2. [Python environment](#python-environment)
   3. [PyCharm](#pycharm)
   4. [AlphaBuild Maintenance](#alphabuild-maintenance)

## Frequent Actions

1. **Lint:** Make sure your code complies with the coding standards and run `make lint`.
2. **Test:** Make sure you wrote unit tests and all unit tests pass by running `make test`.

<!-- markdownlint-disable MD033 -->
<details>
  <summary>
    Click to see more advanced usage of AlphaBuild. One can effortlessly narrow down which files lint or test run on.
  </summary>
For example:

- `make lint on={{cookiecutter.project_name}}/hello.py` runs all on the given file.
- `make lint on={{cookiecutter.project_name}}/` runs all linters in the given directory.
- `make lint on="{{cookiecutter.project_name}}/ tests/"` runs all linters on the given directories.
- `make lint on=build*` runs all linters on the results of the glob.
- `make lint on=myspecialdirs` where at the top of the Makefile 
  `myspecialdir=.github/workflows build-support/alpha-build`. Save yourself a bunch of keystrokes by leveraging aliases.
- `make lint since=master` runs all formatters on the diff between the current branch and master.
- `make lint since=HEAD~1` runs all formatters on all files that changed since "2 commits ago".
- `make lint since=--cached` runs all linters on all files that are "git added".
- `make lint on=my_dir/ since=HEAD~2` will run all linters on all files in `my_dir/` that changed since "3 commits ago".
</details>
<!-- markdownlint-disable MD033 -->

## Initial set-up

### Build system

- **Linux, WSL:** Everything should just work.
- **Windows:** 
  1. You need to have `Git Bash` installed.
  2. It is recommended to use everything from `Git Bash` 
  (although one may use `cmd` or `PowerShell` provided `$PATH` is set properly).
  3. Install `Make` for `Git Bash` by running `./build-support/git-bash-utils/install_make.sh`.
- **MacOS:**
  1. Add a few GNU utils to your shell: `brew install findutils grep`

### Python environment

**To reproduce the environment exactly**

Open the console and, in an empty environment, run `make env`. This reproduces your environment according to 
`constraints.txt`. That is, every time one runs `make env` the environment will always resolve identically.

**To modify the environment**

Open the console and, in an empty environment, run `make env-upgrade`. Run this if you add/remove a new dependency or
if you simply want to let `pip` re-resolve (e.g., to upgrade) the environment and dump the new resolution in the lock
file.


### AlphaBuild maintenance

To upgrade AlphaBuild run the following:
```bash
pip install alpha-build-core --target tmp/
tar -xvf tmp/alpha_build_core.tar.gz
rm -rf tmp/
```
