from django.conf.urls import patterns, include, url
from portal import settings

from django.contrib import admin
admin.autodiscover()

from revuo.urls import urlpatterns as revuo_patterns

urlpatterns = patterns('',
    url(r'', include(revuo_patterns, namespace='revuo')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        )
