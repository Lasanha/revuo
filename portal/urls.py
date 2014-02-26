from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from revuo.urls import urlpatterns as revuo_patterns

urlpatterns = patterns('',
    url(r'', include(revuo_patterns)),
    url(r'^admin/', include(admin.site.urls)),
)
