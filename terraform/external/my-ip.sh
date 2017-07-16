#!/usr/bin/env bash

MY_IP="$(dig +short myip.opendns.com @resolver1.opendns.com)"
MY_CIDR="$MY_IP/32"

# Safely produce a JSON object containing the result value.
# jq will ensure that the value is properly quoted
# and escaped to produce a valid JSON string.
jq -n --arg cidr "$MY_CIDR" '{"cidr":$cidr}'
