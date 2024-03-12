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

echo "- Install uv"
vendor/bin/pip install -q -U uv
echo "- Updating pip, setuptools"
vendor/bin/uv pip install --python vendor/bin/python3 -U pip setuptools
echo "- Installing dev and docs dependencies"
vendor/bin/uv pip sync --python vendor/bin/python3 dev-requirements.txt docs-requirements.txt
echo "- Installing app in edit mode"
vendor/bin/uv pip install --python vendor/bin/python3 --no-deps -e .
echo "- Installing pre-commit hook"
vendor/bin/pre-commit install
