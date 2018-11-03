# frozen_string_literal: true

# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set expandtab :

SDIST_FILES = %w[
  hyperbola
  src
  MANIFEST.in
  Pipfile
  Pipfile.lock
  README.md
  manage.py
  package.json
  setup.cfg
  setup.py
  webpack.config.js
  yarn.lock
].freeze

LB_IP = '192.168.10.40'
MYSQL_IP = '192.168.10.30'
APP_IP = '192.168.10.20'

# rubocop:disable Metrics/MethodLength
def ansible_provision(box, host_type)
  box.vm.provision 'ansible-playbook-password', type: 'shell', inline: <<~SHELL
    env #{`venv/bin/dotenv get ANSIBLE_VAULT_PASSWORD`.strip} printenv ANSIBLE_VAULT_PASSWORD > /tmp/vault-password.txt
  SHELL
  box.vm.provision 'bootstrap', type: :ansible_local do |ansible|
    ansible.install_mode = :pip
    ansible.playbook = 'ansible/provision.yml'
    ansible.groups = {
      host_type => ["#{host_type}-local"],
      "#{host_type}:vars" => {
        'ansible_python_interpreter' => '/usr/bin/python3'
      },
      'all_groups:children' => [host_type]
    }
  end
  box.vm.provision 'provision', type: :ansible_local do |ansible|
    ansible.playbook =
      if File.exist?("ansible/#{host_type}-local.yml")
        "ansible/#{host_type}-local.yml"
      else
        "ansible/#{host_type}.yml"
      end
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

  # enable detailed task timing information during ansible runs
  ENV['ANSIBLE_CALLBACK_WHITELIST'] = 'profile_tasks'

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
      # t3.nano only has 512, but more memory is needed to run pipenv
      v.memory = 2048
    end

    SDIST_FILES.each do |f|
      app.vm.provision 'file', source: f,
                               destination: "/tmp/hyperbola/sdist/#{f}"
    end
    app.vm.provision 'shell', inline: <<~SHELL
      sudo rm -rf /hyperbola/sdist
      sudo mkdir -p /hyperbola
      sudo mv /tmp/hyperbola/sdist /hyperbola/sdist
    SHELL

    ansible_provision(app, 'app')

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
        echo '#{MYSQL_IP} mysql.app.hyperboladc.net' | sudo tee -a /etc/hosts
      fi
    SHELL

    # Fixtures
    app.vm.provision 'fixtures', type: 'shell', inline: <<~SHELL
      sudo -H -u hyperbola-app aws s3 cp s3://hyperbola-app-backup-local/v6/local/database/hyperbola-app-2018-10-28T0501Z.json.tar.gz /tmp/hyperbola-seed.json.tar.gz
      tar -xvzf /tmp/hyperbola-seed.json.tar.gz -C /tmp
      cd /hyperbola/app/current
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
