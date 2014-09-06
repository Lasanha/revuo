from django.conf.urls import patterns, include, url
from portal import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # revuo urls
    url(r'', include('revuo.urls', namespace='revuo')),

    # summernote urls
    url(r'^summernote/', include('django_summernote.urls')),

    # password recovery urls
    url(r'^restricted/password/change$', 
        'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^restricted/password/ok$', 
        'django.contrib.auth.views.password_change_done', {}, 
        name='password_change_done'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.STATIC_ROOT}),
    )
