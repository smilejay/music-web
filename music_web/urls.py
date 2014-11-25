from django.conf.urls import patterns, include, url
import api

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'music_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include('api.urls')),
)
