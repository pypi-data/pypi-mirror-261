#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

PYTHON_VERSION=$(cat .python-version)
echo "Installing Python version $PYTHON_VERSION using pyenv"
pyenv install -s "$PYTHON_VERSION"

if [ -d "vendor" ]; then
    echo "Updating Python venv"
else
    echo "Creating Python venv named 'vendor'"
    python3 -m venv vendor
fi

echo "- Updating pip, setuptools"
vendor/bin/pip install -q -U pip setuptools
echo "- Installing dev dependencies"
vendor/bin/pip install -q -r dev-requirements.txt
echo "- Installing docs dependencies"
vendor/bin/pip install -q -r docs-requirements.txt
echo "- Installing app in edit mode"
vendor/bin/pip install -q --no-deps -e .
echo "- Installing pre-commit hook"
vendor/bin/pre-commit install
