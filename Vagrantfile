# frozen_string_literal: true

# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set expandtab :

SDIST_FILES = %w[
  hyperbola/
  src/
  README.md
  manage.py
  package.json
  poetry.lock
  pyproject.toml
  webpack.config.js
  yarn.lock
].freeze

LB_IP = '192.168.10.40'
MYSQL_IP = '192.168.10.30'
APP_IP = '192.168.10.20'

# rubocop:disable Metrics/MethodLength
def ansible_provision(box, host_type)
  box.vm.provision 'ansible-playbook-password', type: 'shell', inline: <<~SHELL
    echo #{`./bin/ansible_vault_password.py`.strip} > /tmp/vault-password.txt
  SHELL
  box.vm.provision 'provision', type: :ansible_local do |ansible|
    ansible.playbook =
      if File.exist?("ansible/#{host_type}-local.yml")
        "ansible/#{host_type}-local.yml"
      else
        "ansible/#{host_type}.yml"
      end
    ansible.playbook_command =
      'ANSIBLE_CALLBACK_WHITELIST=profile_tasks ansible-playbook'
    ansible.galaxy_role_file = 'ansible/requirements.yml'
    ansible.galaxy_roles_path = '/home/vagrant/.ansible'
    ansible.vault_password_file = '/tmp/vault-password.txt'
    ansible.groups = {
      host_type => ["#{host_type}-local"],
      "#{host_type}:vars" => {
        'ansible_python_interpreter' => '/usr/bin/python3',
        'hyperbola_environment' => 'local',
        'app_nginx_domain' => 'local.hyperboladc.net'
      },
      'all_groups:children' => [host_type]
    }
  end
end
# rubocop:enable Metrics/MethodLength

# rubocop:disable Metrics/BlockLength
Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/bionic64'

  config.vm.define 'lb-local' do |lb|
    lb.vm.network 'private_network', ip: LB_IP
    lb.vm.provider 'virtualbox' do |v|
      v.memory = 512
    end

    ansible_provision(lb, 'lb')

    # Service discovery
    lb.vm.provision 'shell', inline: <<~SHELL
      if ! grep -q 'backend.app.hyperboladc.net' /etc/hosts; then
        echo '#{APP_IP} backend.app.hyperboladc.net' | sudo tee -a /etc/hosts
      fi
    SHELL
  end

  config.vm.define 'mysql-local' do |mysql|
    mysql.vm.network 'private_network', ip: MYSQL_IP

    mysql.vm.provider 'virtualbox' do |v|
      v.memory = 1024
    end

    ansible_provision(mysql, 'mysql')
  end

  config.vm.define 'app-local' do |app|
    app.vm.network 'private_network', ip: APP_IP

    app.vm.provider 'virtualbox' do |v|
      # t3.nano only has 512, but more memory is needed to install dependencies
      v.memory = 2048
    end

    SDIST_FILES.each do |f|
      dest = +'/tmp/hyperbola/sdist/'
      dest << f if f[-1] != '/'
      app.vm.provision 'file', source: f, destination: dest
    end
    app.vm.provision 'shell', inline: <<~SHELL
      sudo rm -rf /hyperbola/sdist
      sudo mkdir -p /hyperbola
      sudo mv /tmp/hyperbola/sdist /hyperbola/sdist
    SHELL

    ansible_provision(app, 'app')

    # Service discovery
    app.vm.provision 'shell', inline: <<~SHELL
      if ! grep -q 'mysql.app.hyperboladc.net' /etc/hosts; then
        echo '#{MYSQL_IP} mysql.app.hyperboladc.net' | sudo tee -a /etc/hosts
      fi
    SHELL

    # Fixtures
    app.vm.provision 'fixtures', type: 'shell', inline: <<~SHELL
      cd /hyperbola/app/current
      export ENVIRONMENT=local
      set -a
      source .env
      aws s3 cp s3://hyperbola-app-backup-local/v6/local/database/hyperbola-app-2018-10-28T0501Z.json.tar.gz /tmp/hyperbola-seed.json.tar.gz
      tar -xvzf /tmp/hyperbola-seed.json.tar.gz -C /tmp
      venv/bin/python manage.py migrate frontpage zero
      venv/bin/python manage.py migrate contact zero
      venv/bin/python manage.py migrate lifestream zero
      venv/bin/python manage.py migrate blog zero
      venv/bin/python manage.py migrate
      venv/bin/python manage.py loaddata /tmp/hyperbola-app-*.json
      venv/bin/python manage.py createcachetable
      rm /tmp/hyperbola*.json*
    SHELL
  end
end
# rubocop:enable Metrics/BlockLength
