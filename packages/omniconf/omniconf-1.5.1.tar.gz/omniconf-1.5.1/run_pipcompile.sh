#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

COMPILE_OPTS=(
  "-q"
  "--strip-extras"
  "--resolver=backtracking"
  "--no-header"
  "--no-emit-package=pip"
  "--no-emit-package=setuptools"
)

for f in dev-requirements.in docs-requirements.in; do
    echo "Building requirements file from $f"
    uv pip compile "${COMPILE_OPTS[@]}" "$@" "$f" -o "${f%%.*}.txt"
    echo
done
