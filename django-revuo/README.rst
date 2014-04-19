=====
Revuo
=====

Revuo is a simple CMS app for Django.

Quick start
-----------

1. Add 'revuo' to your INSTALLED_APPS settings like this:

    INSTALLED_APPS = {
        ...
        'revuo',
    }

2. Import and include revuo urls in your urls.py like this:

    from revuo.urls import urlpatterns as revuo_patterns

    ...

    url(r'', include(revuo_patterns)),

3. Run 'python manage.py syncdb' to create revuo models

4. Start the server
