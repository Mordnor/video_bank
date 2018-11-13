"""
Django settings for video_bank project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '34p6&mgc2^@+$uvdtnpd1c%m7=2iwjy6c^cfe-y@qrhf15&x36'

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
    'django.contrib.sites',


    'video_store',

    'userena',
    'guardian',
    'easy_thumbnails',
    'autoslug',
    'parler',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

# Userena
# https://django-userena-ce.readthedocs.io/en/latest/index.html



AUTHENTICATION_BACKENDS = (  
    'userena.backends.UserenaAuthenticationBackend',  
    'guardian.backends.ObjectPermissionBackend',  
    'django.contrib.auth.backends.ModelBackend',  
)  

ANONYMOUS_USER_NAME = 'anonymous'

AUTH_PROFILE_MODULE  = 'video_store.Customer'



ROOT_URLCONF = 'video_bank.urls'

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
        },
    },
]

WSGI_APPLICATION = 'video_bank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/
from django.utils.translation import ugettext_lazy as _

LOCALE_PATHS = ( os.path.join(BASE_DIR, 'locale'), )

LANGUAGE_CODE = 'fr'

LANGUAGES = [
    ('fr', _('Francais')),
    ('en', _('Anglais')),
]

PARLER_LANGUAGES = {
    1: (
        {'code': 'fr',},
        {'code': 'en',},
        
    ),
    'default': {
        'fallbacks': ['fr'],          # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
    }
}


TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = 'media/'

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "node_modules"),
   os.path.join(BASE_DIR, "media"),
]

LOGIN_URL = "/login"
LOGOUT_URL = "/logout"


# Userena Settings

USERENA_SIGNIN_AFTER_SIGNUP = True
USERENA_ACTIVATION_REQUIRED = False
SITE_ID = 1

