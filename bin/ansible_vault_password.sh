#!/usr/bin/env bash

unset CDPATH

BIN_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# shellcheck disable=SC2016
exec "$BIN_ROOT/artifact-exec" "bash" "-c" '[[ -n "$ANSIBLE_VAULT_PASSWORD" ]] && echo "$ANSIBLE_VAULT_PASSWORD"'
