from django.conf.urls import patterns, include, url
from portal import settings

from django.contrib import admin
admin.autodiscover()

from revuo.urls import urlpatterns as revuo_patterns

urlpatterns = patterns('',
    url(r'', include(revuo_patterns)),
    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        )
