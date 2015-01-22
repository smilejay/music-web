'''
Created on Jan 15, 2015

@author: Jay <smile665@gmail.com>
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url('^add_user', 'api.user_views.add_user'),
    url('^get_user', 'api.user_views.get_user_by_openid'),
)