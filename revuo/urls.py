from django.conf.urls import patterns, include, url

from views import Home, Publications, Staff, StaffView
from views import ItemList, ItemView

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^publications$', Publications.as_view()),
    url(r'^(?P<category>news|blog|media)$', ItemList.as_view()),
    url(r'^(?P<category>[VNB])/(?P<item_id>\d+)$', ItemView.as_view()),
    url(r'^staff$', Staff.as_view()),
    url(r'^staff/(?P<staff_id>\d+)$', StaffView.as_view()),
)
