#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

for f in dev-requirements.in docs-requirements.in; do
    echo "Building requirements file from $f"
    pip-compile -q --strip-extras --resolver=backtracking "$@" $f
    echo
done
