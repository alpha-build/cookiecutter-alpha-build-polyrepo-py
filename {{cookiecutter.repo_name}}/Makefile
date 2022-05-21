SHELL := /usr/bin/env bash
MAKEFLAGS += -j1

include build-support/alpha-build/core/resolver.mk  # Utilities to resolve targets

PY_SOURCES_ROOTS={{cookiecutter.project_name}}/
include build-support/alpha-build/core/python/pythonpath.mk  # Let AlphaBuild set PYTHONPATH based on PY_SOURCES_ROOTS

include build-support/alpha-build/core/multi/pre-commit.mk
include build-support/alpha-build/core/python/test.mk

# Define where Python files live (for testing purposes)
ONPY={{cookiecutter.project_name}}/ tests/

.PHONY: lint
lint: pre-commit-run  # The pre-commit-run goal comes from AlphaBuild Core

.PHONY: test
test: pytest  # The pytest goal comes from AlphaBuild Core

.PHONY: env
env:
	$(python) -m pip install --upgrade pip setuptools
	$(python) -m pip install -r requirements.txt -r requirements-dev.txt -c constraints.txt

.PHONY: env-upgrade
env-upgrade:
	$(python) -m pip install --upgrade pip setuptools
	$(python) -m pip install -r requirements.txt -r requirements-dev.txt
	$(python) -m pip list --format=freeze > constraints.txt
