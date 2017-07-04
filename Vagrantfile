# frozen_string_literal: true

# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set expandtab :

Vagrant.configure('2') do |config|
  config.vm.box = 'ubuntu/xenial64'

  # enable detailed task timing information during ansible runs
  ENV['ANSIBLE_CALLBACK_WHITELIST'] = 'profile_tasks'

  config.vm.define 'wiki-test-1' do |wiki|
    wiki.vm.network 'private_network', ip: '192.168.10.10'

    wiki.vm.provision 'bootstrap', type: 'ansible' do |ansible|
      ansible.verbose = 'v'
      ansible.playbook = 'ansible/provision.yml'
      ansible.groups = {
        'wiki' => ['wiki-test-1'],
        'all_groups:children' => ['wiki']
      }
    end

    wiki.vm.provision 'wiki', type: 'ansible' do |ansible|
      ansible.verbose = 'v'
      ansible.playbook = 'ansible/wiki.yml'
      ansible.vault_password_file = '.secrets/vault-password.txt'
      ansible.groups = {
        'wiki' => ['wiki-test-1'],
        'wiki:vars' => {
          'hyperbola_environment' => 'localhost',
          'wiki_nginx_domain' => 'wiki.local.hyperboladc.net'
        },
        'all_groups:children' => ['wiki']
      }
    end
  end
end
