#!/usr/bin/env bash
set -eu

echo "Starting final pre-PR validation for the Book API documentation sync..."
python -m pytest tests/ -v

if [ -n "$(git status --porcelain)" ]; then
	echo "Pre-PR validation failed: the Git working tree is not clean." >&2
	git status --short
	exit 1
fi

echo "Final pre-PR validation passed; the Git working tree is clean."
