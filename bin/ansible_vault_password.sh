#!/usr/bin/env bash

unset CDPATH

ARTIFACT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ ! -d "$ARTIFACT_ROOT/env" ]]; then
	echo >&2 "No env directory to source"
	echo >&2 "ARTIFACT_ROOT=$ARTIFACT_ROOT"
	exit 1
fi

for env in "$ARTIFACT_ROOT/env/"*.env; do
	# shellcheck source=/dev/null
	. "$env"
done

if [[ -z "$ANSIBLE_VAULT_PASSWORD" ]]; then
	echo &>2 "ANSIBLE_VAULT_PASSWORD not set"
	exit 1
fi

echo "$ANSIBLE_VAULT_PASSWORD"
