from django.conf.urls import url
from django.contrib.auth.views import login, logout

from revuo.views import (
    Dashboard, Home, Publisher,
    ItemList, ItemNew, ItemEdit, ItemPublish, ItemSuspend, ItemDelete, ItemView,
    StaffList, StaffEdit, StaffView,
)

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^news$', ItemList.as_view(category='news'), name='news'),
    url(r'^blog$', ItemList.as_view(category='blog'), name='blog'),
    url(r'^publications$', ItemList.as_view(category='publications'), name='publications'),
    url(r'^(?P<category>[NBP])/(?P<item_id>\d+)$', ItemView.as_view(), name='item_view'),
    url(r'^staff$', StaffList.as_view(), name='staff'),
    url(r'^staff/(?P<staff_id>\d+)$', StaffView.as_view(), name='staff_view'),
    url(r'^restricted/N/add$', ItemNew.as_view(category='N'), name='add_news'),
    url(r'^restricted/B/add$', ItemNew.as_view(category='B'), name='add_blog'),
    url(r'^restricted/P/add$', ItemNew.as_view(category='P'), name='add_publication'),
    url(r'^restricted/edit/(?P<category>[NBP])/(?P<item_id>\d+)$', ItemEdit.as_view(), name='item_edit'),
    url(r'^restricted/edit_profile$', StaffEdit.as_view(), name='edit_profile'),
    url(r'^restricted/publisher$', Publisher.as_view(), name='publisher'),
    url(r'^restricted/publisher/(?P<category>[NBP])/(?P<item_id>\d+)$', ItemPublish.as_view(), name='publish_item'),
    url(r'^restricted/suspender/(?P<category>[NBP])/(?P<item_id>\d+)$', ItemSuspend.as_view(), name='suspend_item'),
    url(r'^restricted/deleter/(?P<category>[NBP])/(?P<item_id>\d+)$', ItemDelete.as_view(), name='trash_item'),
    url(r'^restricted/dashboard$', Dashboard.as_view(), name='dashboard'),

    url(r'login/', login, name='login'),
    url(r'logout/', logout, {'next_page': '/'}, name='logout'),
]

