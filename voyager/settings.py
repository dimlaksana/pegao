"""
Django settings for voyager project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

try:
   from voyager.registry import *
except ImportError:
    raise Exception("A registry file is required to run this project!")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = REG_SECRET_KEY


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = REG_DEBUG

ALLOWED_HOSTS = REG_ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'dione',
    'hiperion',
    'rest_framework',
    'social_django',
]

MIDDLEWARE = [
    'bugsnag.django.middleware.BugsnagMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'voyager.urls'

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
                'social_django.context_processors.backends', #para usar OAuth
                'social_django.context_processors.login_redirect', #para usar OAuth
            ],
        },
    },
]

WSGI_APPLICATION = 'voyager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', #'django.db.backends.sqlite3',
        'NAME': REG_DATABASE_NAME,
        'USER': REG_DATABASE_USER,
        'PASSWORD': REG_DATABASE_PW,
        'HOST': REG_DATABASE_HOST,
        'PORT': '',
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

STATIC_URL = '/static/'

#Gonzalo A. Feb 2019
STATIC_ROOT = os.path.join(BASE_DIR, 'static/') #se requiere para Nginx

MEDIA_URL = '/media/' #archivos cargados por ej foto de perfil
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'hiperion.User'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/' #cuando se logee va a la raiz
#LOGOUT_REDIRECT_URL = '/'

#para usar OAuth
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend', #para poder seguir usando la clave y usuario y poder ingresar al sitio admin
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '65545908578-rdnfspb07n77lf4g4iubvc29u4kq85kf.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Ar2qeCzq6bLxnzZYn9MPFNle'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',

    'hiperion.pipeline.get_avatar',
)

if not DEBUG:
    #Recomendaciones para produccion al ejecutar python manage.py check --deploy
    SECURE_BROWSER_XSS_FILTER = True #True => set the X-XSS-Protection: 1; mode=block header on all responses
    SECURE_CONTENT_TYPE_NOSNIFF = True #True => set the X-Content-Type-Options: nosniff header on all responses
    SECURE_SSL_REDIRECT = True #True => redirect all non-HTTPS requests to HTTPS
    SECURE_HSTS_SECONDS = 60 # non-zero => set the HTTP Strict Transport Security header on all responses
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True #True => add the includeSubDomains tag to the HTTP Strict Transport Security header
    SECURE_HSTS_PRELOAD = True #True => adds the preload directive to the HTTP Strict Transport Security header
    SESSION_COOKIE_SECURE = True #True => the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent under an HTTPS connection
    CSRF_COOKIE_SECURE = True #True => the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent with an HTTPS connection
    X_FRAME_OPTIONS = 'DENY' #set the same X-Frame-Options value for all responses in your site


    #seguimiento a errores
    BUGSNAG = {
        'api_key': BUGSNAG_API_KEY,
        'project_root': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        'root': {
            'level': 'ERROR',
            'handlers': ['bugsnag'],
        },

        'handlers': {
            'bugsnag': {
                'level': 'INFO',
                'class': 'bugsnag.handlers.BugsnagHandler',
            },
        }
    }
