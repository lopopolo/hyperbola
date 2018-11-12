## Lab environment

The lab environment is intended to be a cleanroom for testing terraform
configuration and experimenting with new setups without affecting production
environments like `app-prod-pdx`.

One use of the lab is to ensure that terraform modules have no hidden
dependencies and can come up cleanly from an empty state.
