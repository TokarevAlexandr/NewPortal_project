"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'django_filters',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 5


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
#ACCOUNT_EMAIL_VERIFICATION = 'none'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #smtp/console

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

SITE_URL = 'http://127.0.0.1:8000/'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

import logging

logger = logging.getLogger("django")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "style": "{",
    # -----filters-------------------------------------------------
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        }
    },
    # -----formatters-------------------------------------------------
    "formatters": {
        "DEBUG_log": {
            # все сообщения уровня DEBUG и выше, включающие время, уровень сообщения, сообщения.
            "format": "%(asctime)s - %(levelname)s, Message: %(message)s",
        },
        "INFO_log": {
            # все сообщения уровня DEBUG и дополнительно должен выводиться путь к источнику события.
            "format": '%(asctime)s - %(levelname)s, Module: "%(module)s", Message: %(message)s',
        },
        "WARNING_log": {
            # сообщений WARNING и выше дополнительно должен выводиться путь к источнику события
            # (используется аргумент pathname в форматировании
            "format": "Path %(pathname)s",
        },
        "ERROR_log": {
            # для сообщений ERROR и CRITICAL еще должен выводить
            # стэк ошибки (аргумент exc_info)
            "format": "%(asctime)s, %(levelname)s, %(pathname)s, %(message)s, %(exc_info)s",
        },
    },
    # ----handlers--------------------------------------------------
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "DEBUG_log",
        },
        "console_warning": {
            "level": "WARNING",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "WARNING_log",
        },
        # с указанием времени, уровня логирования, модуля, в котором возникло сообщение (аргумент module) и само сообщение
        "general_log_file": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.FileHandler",
            "formatter": "INFO_log",
            "filename": "general.log",
        },
        "warning_to_file": {
            "level": "WARNING",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "formatter": "WARNING_log",
            "filename": "general.log",
        },
        "errors_log_file": {
            "level": "ERROR", #"INFO", for test
            "class": "logging.FileHandler",
            "formatter": "ERROR_log",
            "filename": "errors.log",
        },
        "security_log_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "formatter": "ERROR_log",
            "filename": "security.log",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
            "email_backend": "django.core.mail.backends.filebased.EmailBackend",
            "formatter": "ERROR_log",
        },
    },
    # -----loggers-------------------------------------------------
    "loggers": {
        "django": {
            "handlers": [
                "console",
                "console_warning",
                "general_log_file",
                "warning_to_file",
            ],
            "propagate": True,
        },
        "django.template": {
            "handlers": ["errors_log_file"],
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["errors_log_file"],
            "propagate": False,
        },
        "django.server": {
            "handlers": ["mail_admins", "errors_log_file"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins", "errors_log_file"],
            "propagate": False,
        },
        "django.security": {
            "handlers": ["security_log_file"],
            "propagate": False,
        },
    },
}
# Application definition
