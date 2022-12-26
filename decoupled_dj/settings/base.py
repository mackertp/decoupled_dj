"""
This is the base settings file.

To select the development settings for use, we will run 
'export DJANGO_SETTINGS_MODULE=decoupled_dj.settings.development'
from the terminal. Obviously, we can replace that when the
time comes for deployment.

@author Preston Mackert
"""

# --------------------------------------------------- #
# imports
# --------------------------------------------------- #

import environ
from pathlib import Path


# --------------------------------------------------- #
# environment setup
# --------------------------------------------------- #

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", False)


# --------------------------------------------------- #
# applications
# --------------------------------------------------- #

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users.apps.UsersConfig",
]


# --------------------------------------------------- #
# middleware
# --------------------------------------------------- #

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------- #
# url routing & templates
# --------------------------------------------------- #

ROOT_URLCONF = 'decoupled_dj.urls'

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


# --------------------------------------------------- #
# middleware
# --------------------------------------------------- #

WSGI_APPLICATION = 'decoupled_dj.wsgi.application'


# --------------------------------------------------- #
# database config
# --------------------------------------------------- #

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
        }
    }


# --------------------------------------------------- #
# database config
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
# --------------------------------------------------- #

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


# --------------------------------------------------- #
# internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# --------------------------------------------------- #

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# --------------------------------------------------- #
# static url - html, css, javascript
# --------------------------------------------------- #

STATIC_URL = '/static/'


# --------------------------------------------------- #
# default primary key type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
# --------------------------------------------------- #

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --------------------------------------------------- #
# set custom user model
# --------------------------------------------------- #

AUTH_USER_MODEL = "users.User"