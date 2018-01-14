# frozen_string_literal: true

# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set expandtab :

# https://stackoverflow.com/a/38203497
# Function to check whether VM was already provisioned
def provisioned?(vm_name = 'default', provider = 'virtualbox')
  File.exist?(".vagrant/machines/#{vm_name}/#{provider}/action_provision")
end

# rubocop:disable Metrics/BlockLength
Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/xenial64'

  # enable detailed task timing information during ansible runs
  ENV['ANSIBLE_CALLBACK_WHITELIST'] = 'profile_tasks'

  config.vm.define 'mysql-local' do |mysql|
    mysql.vm.network 'private_network', ip: '192.168.10.30'
    mysql.vm.network 'forwarded_port', guest: 3306, host: 13306

    mysql.vm.provision 'mysql-local', type: 'ansible' do |ansible|
      ansible.verbose = 'v'
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

    app.vm.provision 'bootstrap', type: 'ansible' do |ansible|
      ansible.verbose = 'v'
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
      ansible.verbose = 'v'
      ansible.playbook = 'ansible/app.yml'
      ansible.vault_password_file = 'bin/ansible_vault_password.py'
      ansible.groups = {
        'app' => ['app-local'],
        'app:vars' => {
          'ansible_python_interpreter' => '/usr/bin/python3',
          'hyperbola_environment' => 'local',
          'app_nginx_domain' => 'app-local.hyperboladc.net'
        },
        'all_groups:children' => ['app']
      }
    end

    app.vm.provision 'file', source: '~/.aws', destination: '/tmp/aws-creds'
    app.vm.provision 'shell', inline: <<~SHELL
      rm -rf /home/hyperbola-app/.aws
      mv /tmp/aws-creds/ /home/hyperbola-app/.aws
      chown -R hyperbola-app:hyperbola-app /home/hyperbola-app/.aws
      chmod -R u=rX,go=X /home/hyperbola-app
    SHELL
    app.vm.provision 'shell', inline: <<~SHELL
      sudo -H -u hyperbola-app aws s3 cp s3://hyperbola-app-backup-local/v5/local/database/hyperbola-app-2017-12-03T0126Z.json /tmp/hyperbola-seed.json
      cd /hyperbola/app/current
      venv/bin/python manage.py migrate
      venv/bin/python manage.py loaddata /tmp/hyperbola-seed.json
      venv/bin/python manage.py createcachetable
    SHELL
  end
end
