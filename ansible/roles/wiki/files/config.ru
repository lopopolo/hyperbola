#!/usr/bin/env ruby
# frozen_string_literal: true

require 'rubygems'
require 'gollum/app'
require 'rack/ssl'
require 'socket'

# HyperbolaMiddleware adds gollum author information to the current session
# and adds a comment to resulting HTML with the canonical hostname of the
# machine that served the request.
class HyperbolaMiddleware
  def initialize(app)
    @app = app
    @fqdn = Socket.gethostname
    @users = {
      'lopopolo' => { name: 'Ryan Lopopolo (gollum)', email: 'rjl@hyperbo.la' }
    }
  end

  def call(env)
    if @users.key? env['HTTP_X_FORWARDED_USER']
      env['rack.session'] ||= {}
      env['rack.session']['gollum.author'] = @users[env['HTTP_X_FORWARDED_USER']]
    end
    status, headers, response = @app.call(env)
    if headers['Content-Type'] =~ %r{text/html|application/xhtml+xml}
      response, updated_headers = insert_comment(response)
      headers.merge! updated_headers
    end
    [status, headers, response]
  end

  def insert_comment(response)
    body = ''
    response.each { |part| body << part }
    index = body.rindex('</body>')
    return response, {} unless index
    body.insert(index, "<!-- canonical hostname: #{@fqdn} -->")
    [[body], { 'Content-Length' => body.length.to_s }]
  end
end

GOLLUM_PATH = '/hyperbola/wiki.hyperbo.la/wiki'

Precious::App.set(:gollum_path, GOLLUM_PATH)
Precious::App.set(:default_markup, :markdown)
Precious::App.set(:wiki_options, universal_toc: false, live_preview: false)

Gollum::Hook.register(:post_commit, :git_resync) do
  puts `git-resync`
end

$stdout.sync = true
$stderr.sync = true

app = Rack::Builder.new do
  map '/' do
    use HyperbolaMiddleware
    use Rack::SSL, hsts: false
    run Precious::App
  end

  map '/healthz' do
    run ->(_env) { [200, { 'Content-Type' => 'text/plain' }, ['OK']] }
  end
end

run app
