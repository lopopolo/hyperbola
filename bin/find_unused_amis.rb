#!/usr/bin/env ruby -W0
# frozen_string_literal: true

require 'aws-sdk-v1'

client = AWS::EC2.new
amis = client.instances.map do |instance|
  begin
    instance.image_id
  rescue AWS::Core::Resource::NotFound
    nil
  end
end.compact.uniq

puts '# Loading available AMIs...'
images = client.images.with_owner('self').sort_by(&:name)
images.each do |image|
  next if amis.include?(image.id)
  fields = [
    image.id,
    image.block_device_mappings.values.map(&:snapshot_id).compact.join(','),
    image.name
  ]

  puts(fields.join("\t"))
end