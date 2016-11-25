#!/usr/bin/env ruby -W0

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
images = client.images.with_owner('self').sort_by { |i| i.name }
images.each do |image|
  next if amis.include?(image.id)
  fields = []
  fields << image.id
  fields << image.block_device_mappings.values.map(&:snapshot_id).compact.join(',')
  fields << image.name

  puts(fields.join("\t"))
end
