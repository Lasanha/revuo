import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['REVUO_KEY']

DEBUG = os.environ.get('REVUO_DEBUG', False)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['revuo.herokuapp.com']

INSTALLED_APPS = (
    'revuo',
    'django_summernote',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'portal.urls'

WSGI_APPLICATION = 'portal.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'mediafiles'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        }
    }
]

LOGIN_URL = '/login/'

if DEBUG:
    debug_db = os.path.join(BASE_DIR, 'db.sqlite3')
    DATABASES = {'default': {'ENGINE':'django.db.backends.sqlite3', 'NAME': debug_db,}}
else:
    import dj_database_url
    db_url = os.environ['DATABASE_URL']
    DATABASES = {'default': dj_database_url.config(default=db_url)}
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_S3_HOST = os.environ['AWS_S3_HOST']
    AWS_QUERYSTRING_AUTH = False
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
    INSTALLED_APPS += ('storages',)
    STATIC_URL = S3_URL
    MEDIA_URL = S3_URL + 'media/'
    DEFAULT_FILE_STORAGE = 'portal.s3utils.MediaS3BotoStorage'

    SUMMERNOTE_CONFIG = {
        'attachment_storage_class': 'portal.s3utils.MediaS3BotoStorage',
    }
