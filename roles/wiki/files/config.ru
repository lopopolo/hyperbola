#!/usr/bin/env ruby

require 'rubygems'
require 'gollum/app'
require 'rack/ssl'

class LopopoloGollumAuthor
  def initialize(app)
    @app = app
  end

  def call(env)
    env['rack.session'] ||= {}
    env['rack.session']['gollum.author'] = {
        name: 'Ryan Lopopolo (gollum)',
        email: 'rjl@hyperbo.la'
    }
    @app.call(env)
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

use LopopoloGollumAuthor
use Rack::SSL, hsts: false unless ENV['RACK_ENV'] == 'localhost'
run Precious::App
