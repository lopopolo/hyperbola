#!/usr/bin/env ruby -W0

require 'aws-sdk-v1'

if ARGV.empty?
  puts "USAGE: #{$PROGRAM_NAME} ami-id ami-id ..."
  exit(1)
end

client = AWS::EC2.new
ARGV.each do |ami_id|
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
end
