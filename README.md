revuo
=====

Plug and play, simple portal and blog django-app

This repo is an example installation. You can see two distinct configurations on portal/settings.py: 
for DEBUG=True, local sqlite3 for database (that's used on travis-ci); for DEBUG=False, remote postgres 
for database and S3 for static and media storage (that I used when deploying to Heroku).

If you want just the app, code is on revuo directory and it is totally uncoupled from these configurations. 
You can also install from PyPI with
> pip install django-revuo

[![Build Status](https://travis-ci.org/Lasanha/revuo.png?branch=master)](https://travis-ci.org/Lasanha/revuo)

[![Coverage Status](https://coveralls.io/repos/Lasanha/revuo/badge.png)](https://coveralls.io/r/Lasanha/revuo)

[![Requirements Status](https://requires.io/github/Lasanha/revuo/requirements.png?branch=master)](https://requires.io/github/Lasanha/revuo/requirements/?branch=master)
