=====
Revuo
=====

Revuo is a simple CMS app for Django.

News
----

Version 0.2.1 -
* test updates, passing with django 1.7

Version 0.2 -
* using summernote wysiwyg editor
* removing Video items, because it easy to embed them on news or posts

Version 0.1.1 -

* styling pages
* static handling

Version 0.1 - 

basic, first version

Quick start
-----------

1. Add revuo and summernote to your INSTALLED_APPS settings like this:

    INSTALLED_APPS = {
        ...
        'revuo',
        'django_summernote',
    }

2. Import and include revuo and summernote urls in your urls.py like this:

    from revuo.urls import urlpatterns as revuo_patterns

    ...

    # revuo urls
    url(r'', include(revuo_patterns, namespace='revuo')),

    # summernote urls
    url(r'^summernote/', include('django_summernote.urls')),

    # password recovery urls
    url(r'^restricted/password/change$', 
        'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^restricted/password/ok$', 
        'django.contrib.auth.views.password_change_done', {}, 
        name='password_change_done'),

3. Run 'python manage.py syncdb' to create revuo models

4. Start the server
