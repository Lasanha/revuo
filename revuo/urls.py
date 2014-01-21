from django.conf.urls import patterns, include, url

from views import Home, News, Media, Publications, Blog, Staff

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^news$', News.as_view()),
    url(r'^media$', Media.as_view()),
    url(r'^publications$', Publications.as_view()),
    url(r'^blog$', Blog.as_view()),
    url(r'^staff$', Staff.as_view()),
)
