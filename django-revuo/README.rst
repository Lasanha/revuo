=====
Revuo
=====

Revuo is a simple CMS app for Django.

News
----

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

2. Import and include revuo urls in your urls.py like this:

    from revuo.urls import urlpatterns as revuo_patterns

    ...

    url(r'', include(revuo_patterns)),

3. Run 'python manage.py syncdb' to create revuo models

4. Start the server
