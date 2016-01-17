from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import password_change, password_change_done
from django.views.static import serve as static_serve

from django_summernote import urls as summernote_urls

from portal import settings
from revuo.urls import urlpatterns as revuo_urls

admin.autodiscover()

urlpatterns = [
    # revuo urls
    url(r'', include(revuo_urls, namespace='revuo')),

    # summernote urls
    url(r'^summernote/', include(summernote_urls)),

    # password recovery urls
    url(r'^restricted/password/change$', password_change, name='password_change'),
    url(r'^restricted/password/ok$', password_change_done, {}, name='password_change_done'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
]

if not settings.DEBUG:
    urlpatterns += [(r'^static/(?P<path>.*)$', static_serve, {'document_root': settings.STATIC_ROOT})]
