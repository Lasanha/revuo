from django.conf.urls import patterns, include, url

from views import Home, News, NewsItem, Media, Publications, Blog, Staff
from views import BlogItem, MediaItem

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^news$', News.as_view()),
    url(r'^news/(?P<news_id>\d+)$', NewsItem.as_view()),
    url(r'^media$', Media.as_view()),
    url(r'^media/(?P<media_id>\d+)$', MediaItem.as_view()),
    url(r'^publications$', Publications.as_view()),
    url(r'^blog$', Blog.as_view()),
    url(r'^blog/(?P<post_id>\d+)$', BlogItem.as_view()),
    url(r'^staff$', Staff.as_view()),
)
