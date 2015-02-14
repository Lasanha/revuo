from django.conf.urls import patterns, url

from revuo.views import Home, Staff, StaffView
from revuo.views import ItemList, ItemView, NewItem, ItemEdit
from revuo.views import EditProfile, Publisher, PublishItem, SuspendItem, TrashItem, Dashboard

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^news$', ItemList.as_view(category='news'), name='news'),
    url(r'^blog$', ItemList.as_view(category='blog'), name='blog'),
    url(r'^publications$', ItemList.as_view(category='publications'), name='publications'),
    url(r'^(?P<category>[NBP])/(?P<item_id>\d+)$', ItemView.as_view(), name='item_view'),
    url(r'^staff$', Staff.as_view(), name='staff'),
    url(r'^staff/(?P<staff_id>\d+)$', StaffView.as_view(), name='staff_view'),
    url(r'^restricted/N/add$', NewItem.as_view(category='N'), name='add_news'),
    url(r'^restricted/B/add$', NewItem.as_view(category='B'), name='add_blog'),
    url(r'^restricted/P/add$', NewItem.as_view(category='P'), name='add_publication'),
    url(r'^restricted/edit/(?P<category>[NBP])/(?P<item_id>\d+)$', ItemEdit.as_view(), name='item_edit'),
    url(r'^restricted/editprofile$', EditProfile.as_view(), name='edit_profile'),
    url(r'^restricted/publisher$', Publisher.as_view(), name='publisher'),
    url(r'^restricted/publisher/(?P<category>[NBP])/(?P<item_id>\d+)$', PublishItem.as_view(), name='publish_item'),
    url(r'^restricted/suspender/(?P<category>[NBP])/(?P<item_id>\d+)$', SuspendItem.as_view(), name='suspend_item'),
    url(r'^restricted/dashboard$', Dashboard.as_view(), name='dashboard'),
    url(r'^restricted/trasher/(?P<category>[NBP])/(?P<item_id>\d+)$', TrashItem.as_view(), name='trash_item'),

    url(r'login/', 'django.contrib.auth.views.login', name='login'),
    url(r'logout/', 'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),

)
