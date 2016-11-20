.PHONY: install_roles

install_roles:
	ansible-galaxy install -r roles/requirements.yml -p ./roles/ --force
