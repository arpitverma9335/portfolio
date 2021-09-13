"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
#
import os
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'staticfiles/js', 'serviceworker.js')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['secret_key_portfolio']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1' , 'varpit.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'personal',
    'compressor',
    'pwa',
]

PWA_APP_NAME = 'Arpit Verma'
PWA_APP_DESCRIPTION = "Arpit Verma Personal Portfolio" 
PWA_APP_THEME_COLOR = '#0A0302' 
PWA_APP_BACKGROUND_COLOR = '#ffffff' 
PWA_APP_DISPLAY = 'standalone' 
#PWA_APP_SCOPE = '/' 
PWA_APP_ORIENTATION = 'any' 
PWA_APP_START_URL = '/' 
PWA_APP_STATUS_BAR_COLOR = 'default' 
PWA_APP_ICONS = [ { 'src': '/static/img/icon_512x512.png', 'sizes': '512x512', "purpose": "any maskable"},
                   { 'src': '/static/img/icon_192x192.png', 'sizes': '192x192', "purpose": "any maskable"},
                   { 'src': '/static/img/icon_160x160.png', 'sizes': '160x160', "purpose": "any maskable"},
                   { 'src': '/static/img/icon_148x148.png', 'sizes': '148x148', "purpose": "any maskable"},
                   { 'src': '/static/img/icon_96x96.png', 'sizes': '96x96', "purpose": "any maskable"} ,
                   { 'src': '/static/img/icon_48x48.png', 'sizes': '48x48', "purpose": "any maskable"} ,
                   { 'src': '/static/img/icon_32x32.png', 'sizes': '32x32', "purpose": "any maskable"} ,
                ] 
PWA_APP_ICONS_APPLE = [ { 'src': '/static/img/icon_192x192.png', 'sizes': '192x192'},
                        { 'src': '/static/img/icon_160x160.png', 'sizes': '160x160'},
                        { 'src': '/static/img/icon_148x148.png', 'sizes': '148x148'},
                        { 'src': '/static/img/icon_96x96.png', 'sizes': '96x96'} ,
                        { 'src': '/static/img/icon_48x48.png', 'sizes': '48x48'} ,
                        { 'src': '/static/img/icon_32x32.png', 'sizes': '32x32'} ] 

PWA_APP_SPLASH_SCREEN = [ { 'src': '/static/img/icon_512x512.png', 'sizes': '512x512'} ] 
PWA_APP_DIR = 'ltr' 
PWA_APP_LANG = 'en-US'

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG is False:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True


ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['db_name'],
        'USER': 'postgres',
        'PASSWORD': os.environ['db_pass'],
        'HOST': 'localhost',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'static_content')
      ]
STATIC_ROOT = os.path.join(BASE_DIR , 'assets')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    # Add this
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_FILTERS = {
    'css':[
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.rCSSMinFilter',
    ],
    'js':[
        'compressor.filters.jsmin.JSMinFilter',
    ]
}
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = False

django_heroku.settings(locals())