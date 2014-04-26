from django.conf.urls import patterns, include, url

from revuo.views import Home, Staff, StaffView
from revuo.views import ItemList, ItemView, NewItem, EditProfile, Publisher, PublishItem, TrashItem

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
    url(r'^(?P<category>publications|news|blog)$', ItemList.as_view()),
    url(r'^(?P<category>[NBP])/(?P<item_id>\d+)$', ItemView.as_view()),
    url(r'^staff$', Staff.as_view()),
    url(r'^staff/(?P<staff_id>\d+)$', StaffView.as_view()),
    url(r'^restricted/(?P<category>[NBP])/add$', NewItem.as_view()),
    url(r'^restricted/editprofile$', EditProfile.as_view()),
    url(r'^restricted/publisher$', Publisher.as_view()),
    url(r'^restricted/publisher/(?P<category>[VNBP])/(?P<item_id>\d+)$', PublishItem.as_view()),
    url(r'^restricted/trasher/(?P<category>[VNBP])/(?P<item_id>\d+)$', TrashItem.as_view()),

    # password change
    url(r'^restricted/password/change$', 'django.contrib.auth.views.password_change'),
    url(r'^restricted/password/ok$', 'django.contrib.auth.views.password_change_done', {}, name='password_change_done'),
    url(r'login/', 'django.contrib.auth.views.login'),
    url(r'logout/', 'django.contrib.auth.views.logout', {'next_page':'/'}),

    # summernote for wysiwyg editor
    url(r'^summernote/', include('django_summernote.urls')),
)
