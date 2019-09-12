"""
Django settings for HireMe project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xw2k4!-vn2sln#6m#&n=$=7wumpa_bycyr8j)$zmpiilwmmn8b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'feed',
    'taggit',
    'crispy_forms',
    # 'location_field.apps.DefaultConfig',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Custom User model
AUTH_USER_MODEL = 'accounts.Client'

# Using this for getting absolute url of person
ABSOLUTE_URL_OVERRIDES = {
 'accounts.Client': lambda u: reverse_lazy('user_detail',
 args=[u.username])
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HireMe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'HireMe', 'base_templates'),
            os.path.join(BASE_DIR, 'accounts', 'templates'),
        ],
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

WSGI_APPLICATION = 'HireMe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'HireMe', 'assets')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#LOCATION_FIELD_PATH = settings.STATIC_URL + 'location_field'

# LOCATION_FIELD = {
#     'map.provider': 'google',
#     'map.zoom': 13,
#
#     'search.provider': 'google',
#     'search.suffix': '',
#
#     # Google
#     'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
#     'provider.google.api_key': '',
#     'provider.google.api_libraries': '',
#     'provider.google.map.type': 'ROADMAP',
#
#     # misc
#     'resources.root_path': LOCATION_FIELD_PATH,
#     'resources.media': {
#         'js': (
#             LOCATION_FIELD_PATH + '/js/jquery.livequery.js',
#             LOCATION_FIELD_PATH + '/js/form.js',
#         ),
#     },
# }