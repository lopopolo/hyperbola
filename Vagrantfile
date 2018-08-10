# frozen_string_literal: true

# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set expandtab :

# https://stackoverflow.com/a/38203497
# Function to check whether VM was already provisioned
def provisioned?(vm_name = 'default', provider = 'virtualbox')
  File.exist?(".vagrant/machines/#{vm_name}/#{provider}/action_provision")
end

def verbose(ansible)
  # ansible.verbose = 'v'
end

# rubocop:disable Metrics/BlockLength
Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/bionic64'

  # enable detailed task timing information during ansible runs
  ENV['ANSIBLE_CALLBACK_WHITELIST'] = 'profile_tasks'

  config.vm.define 'lb-local' do |lb|
    lb.vm.network 'private_network', ip: '192.168.10.40'

    lb.vm.provider 'virtualbox' do |v|
      v.memory = 512
    end

    lb.vm.provision 'bootstrap', type: 'ansible' do |ansible|
      verbose(ansible)
      ansible.playbook = 'ansible/provision.yml'
      ansible.groups = {
        'lb' => ['lb-local'],
        'lb:vars' => {
          'ansible_python_interpreter' => '/usr/bin/python3'
        },
        'all_groups:children' => ['lb']
      }
    end

    lb.vm.provision 'lb-local', type: 'ansible' do |ansible|
      verbose(ansible)
      ansible.playbook = 'ansible/lb-local.yml'
      ansible.vault_password_file = 'bin/ansible_vault_password.py'
      ansible.groups = {
        'lb' => ['lb-local'],
        'lb:vars' => {
          'ansible_python_interpreter' => '/usr/bin/python3',
        },
        'all_groups:children' => ['lb']
      }
    end

    # Service discovery
    lb.vm.provision 'shell', inline: <<~SHELL
      if ! grep -q 'backend.app.hyperboladc.net' /etc/hosts; then
        echo '192.168.10.20 backend.app.hyperboladc.net' | sudo tee -a /etc/hosts
      fi
    SHELL
  end

  config.vm.define 'mysql-local' do |mysql|
    mysql.vm.network 'private_network', ip: '192.168.10.30'
    mysql.vm.network 'forwarded_port', guest: 3306, host: 13306

    mysql.vm.provider 'virtualbox' do |v|
      v.memory = 512
    end

    mysql.vm.provision 'mysql-local', type: 'ansible' do |ansible|
      verbose(ansible)
      ansible.playbook = 'ansible/mysql-local.yml'
      ansible.vault_password_file = 'bin/ansible_vault_password.py'
      ansible.groups = {
        'mysql' => ['mysql-local'],
        'mysql:vars' => {
          'ansible_python_interpreter' => '/usr/bin/python3',
        },
        'all_groups:children' => ['mysql']
      }
    end
  end

  config.vm.define 'app-local' do |app|
    app.vm.network 'private_network', ip: '192.168.10.20'

    app.vm.provider 'virtualbox' do |v|
      v.memory = 2048
    end

    %w[dist document-root hyperbola MANIFEST.in Pipfile Pipfile.lock README.md manage.py setup.py setup.cfg].each do |f|
      app.vm.provision 'file', source: f, destination: "/tmp/hyperbola/sdist/#{f}"
    end
    app.vm.provision 'shell', inline: <<~SHELL
      sudo rm -rf /hyperbola/sdist
      sudo mv /tmp/hyperbola/sdist /hyperbola/sdist
    SHELL

    app.vm.provision 'bootstrap', type: 'ansible' do |ansible|
      verbose(ansible)
      ansible.playbook = 'ansible/provision.yml'
      ansible.groups = {
        'app' => ['app-local'],
        'app:vars' => {
          'ansible_python_interpreter' => '/usr/bin/python3'
        },
        'all_groups:children' => ['app']
      }
    end

    app.vm.provision 'app-local', type: 'ansible' do |ansible|
      verbose(ansible)
      ansible.playbook = 'ansible/app.yml'
      ansible.vault_password_file = 'bin/ansible_vault_password.py'
      ansible.groups = {
        'app' => ['app-local'],
        'app:vars' => {
          'ansible_python_interpreter' => '/usr/bin/python3',
          'hyperbola_environment' => 'local',
          'app_nginx_domain' => 'local.hyperboladc.net'
        },
        'all_groups:children' => ['app']
      }
    end

    # AWS creds
    app.vm.provision 'file', source: '~/.aws', destination: '/tmp/aws-creds'
    app.vm.provision 'shell', inline: <<~SHELL
      rm -rf /home/hyperbola-app/.aws
      mv /tmp/aws-creds/ /home/hyperbola-app/.aws
      chown -R hyperbola-app:hyperbola-app /home/hyperbola-app/.aws
      chmod -R u=rX,go=X /home/hyperbola-app
    SHELL

    # Service discovery
    app.vm.provision 'shell', inline: <<~SHELL
      if ! grep -q 'mysql.app.hyperboladc.net' /etc/hosts; then
        echo '192.168.10.30 mysql.app.hyperboladc.net' | sudo tee -a /etc/hosts
      fi
    SHELL

    # Fixtures
    app.vm.provision 'fixtures', type: 'shell', inline: <<~SHELL
      sudo -H -u hyperbola-app aws s3 cp s3://hyperbola-app-backup-local/v5/local/database/hyperbola-app-2017-12-03T0126Z.json /tmp/hyperbola-seed.json
      cd /hyperbola/app/current
      venv/bin/python manage.py migrate frontpage zero
      venv/bin/python manage.py migrate contact zero
      venv/bin/python manage.py migrate lifestream zero
      venv/bin/python manage.py migrate
      venv/bin/python manage.py loaddata /tmp/hyperbola-seed.json
      venv/bin/python manage.py createcachetable
      rm /tmp/hyperbola-seed.json
    SHELL
  end
end
