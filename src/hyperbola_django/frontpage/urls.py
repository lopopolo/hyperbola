'''
Created on Dec 16, 2010

@author: Ryan Lopopolo
'''
from django.conf.urls.defaults import patterns

urlpatterns = patterns('frontpage.views',
    (r'^$', 'index'),
)