'''
Created on Jan 15, 2015

@author: Jay <smile665@gmail.com>
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url('^search', 'api.song_views.search'),
)