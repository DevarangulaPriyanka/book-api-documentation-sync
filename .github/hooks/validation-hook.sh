#!/usr/bin/env bash
set -eu

echo "Starting Book API documentation-sync validation..."
python -m pytest tests/ -v
echo "Book API documentation-sync validation passed."
