#!/bin/bash
#
# Usage: python_test.sh

set -e

make test

if [ -n "$COVERALLS_REPO_TOKEN" ]; then
    coveralls
fi
