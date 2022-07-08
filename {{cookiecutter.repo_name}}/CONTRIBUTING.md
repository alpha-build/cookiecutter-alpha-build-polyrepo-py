# Contributing guidelines

## Outline

1. [Frequent actions](#frequent-actions)
2. [Initial set-up](#initial-set-up)
   1. [Build system](#build-system)
   2. [Python environment](#python-environment)
   3. [Pre-commit environment](#pre-commit-environment)
   4. [PyCharm](#pycharm)
   5. [AlphaBuild Maintenance](#alphabuild-maintenance)

## Frequent Actions

1. **Lint:** Make sure your code complies with the coding standards and run `make lint` in the terminal.
2. **Test:** Make sure you wrote unit tests and all unit tests pass by running `make test` in the terminal.
3. **Local multi-env tests:** Test your code locally against multiple Python version by running, from the
   repo root, `nox` or `nox -db conda` if you are using `conda`. See the `nox` docs and the `noxfile.py` to
   understand this better. If you are developing a library this step is particularly important. Conversely, if it is
   an app, the lock files should suffice.

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
- `make lint hook=mypy` runs `mypy` (out of all the linters) all the Python files.
- `make lint hook=mypy on=my_dir/ since=HEAD~2` runs `mypy` on all files in `my_dir/` that changed since
  "3 commits ago".

</details>
<!-- markdownlint-disable MD033 -->

## Initial set-up

### Build system

- **Linux, WSL:** Everything should just work.
- **Windows:**
  1. You need to have `Git Bash` installed.
  2. It is recommended to use everything from `Git Bash`
     (although one may use `cmd` or `PowerShell` provided `$PATH` is set properly).
  3. Install `Make` for `Git Bash` by running `./build-support/git-bash-integration/install_make.sh`.
     Note that you may need to run `Git Bash` as administrator.
- **MacOS:**
  1. Add a few GNU utils to your shell: `brew install findutils grep`

### Python environment

#### To reproduce the environment exactly

Open the console and, in an empty environment, run `make env`. This reproduces your environment according to the lock
file: `3rdparty/constraints.txt`. That is, every time one runs `make env` the environment will always resolve
identically.

#### To amend the environment (upgrade / add / remove packages)

Open the console and, in an empty environment, run `make env-upgrade`. Run this if you add/remove a new dependency or
if you simply want to let `pip` re-resolve (e.g., to upgrade) the environment and dump the new resolution in the lock
file.

### Pre-commit environment

Normally, `pre-commit` installs linters and formatters in a location that is not part of the Python environment. It
relies on specific/pinned versions of these tools. So, from time to time please run `pre-commit autoupdate` to
upgrade the versions of these linters and formatters.

### PyCharm

- **Windows:**

  - You may wish to set the default terminal to `Git Bash`.
    Go to `Settings` (search for "terminal") &#8594; `Tools` &#8594; `Terminal` and change the shell path to
    Git Bash, it must be something like `C:\Program Files\Git\bin\bash.exe`.
    _Note_ that if you are using `conda` to manage your environments `conda activate` will not work in Git Bash inside
    PyCharm but `source activate` will work.
  - Also, it is recommended to set the line endings to _Unix-style_. In Pycharm
    [(see here)](https://www.jetbrains.com/help/pycharm/configuring-line-endings-and-line-separators.html)
    as well as in `git`:

    ```bash
    git config --global core.autocrlf true
    ```

- **All platforms:**

  - Point PyCharm to the Python environment you have just created.
  - Mark your sources roots directories (i.e., the things that would typically go on your `$PYTHONPATH`).
  - Make pytest your default test runner (if PyCharm does not change it automatically).

### AlphaBuild maintenance

To upgrade AlphaBuild run the following:

```bash
pip install alpha-build-core --target tmp/
tar -xvf tmp/alpha_build_core.tar.gz
rm -rf tmp/
```
