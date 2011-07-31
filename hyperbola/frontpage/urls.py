'''
Created on Dec 16, 2010

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import *

urlpatterns = patterns('hyperbola.frontpage.views',
  (r'^$', 'index'),
)
