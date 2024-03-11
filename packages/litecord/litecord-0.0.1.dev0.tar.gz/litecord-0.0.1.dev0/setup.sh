#!/usr/bin/env bash
set -e

if ! command -v rye &>/dev/null; then
    curl -sSf https://rye-up.com/get | bash
    source "$HOME/.rye/env"
fi

rye sync
