#!/usr/bin/env ruby -W0
# frozen_string_literal: true

require 'aws-sdk-v1'

if ARGV.empty?
  puts "USAGE: #{$PROGRAM_NAME} ami-id ami-id ..."
  exit(1)
end

clients = %w[us-east-1 us-west-2].map { |region| AWS::EC2.new(region: region) }
ARGV.each do |ami_id|
  clients.each do |client|
    begin
      image = client.images[ami_id]
      snapshots = image.block_device_mappings.values.map(&:snapshot_id).compact
      puts "Deregistering AMI [#{image.name}] with snapshots #{snapshots.inspect}"
      image.deregister
      puts 'Image deregistered'
      snapshots.each do |snapshot|
        puts "Deleting snapshot #{snapshot}"
        client.snapshots[snapshot].delete
        puts 'Snapshot deleted'
      end
    rescue AWS::EC2::Errors::InvalidAMIID::NotFound
      nil
    end
  end
end
