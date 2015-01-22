from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'music_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^get_songs_by_category/', 'api.views.get_songs_by_category'),
    url(r'^get_songs_by_gender/', 'api.views.get_songs_by_singer_gender'),
    url(r'^get_all_categories/', 'api.views.get_all_categories'),
    url('^user/', include('api.user_urls')),
)
