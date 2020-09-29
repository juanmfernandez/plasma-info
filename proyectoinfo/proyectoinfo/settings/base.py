"""
Django settings for ProyectoInfo project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print('BASE_DIR: ', BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nqe!1!xv1f59(an+1d70)8ql^x4zp3j(3370g*^0+s)bib&yvv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['plasma-info.alwaysdata.net', 'localhost', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyectoinfo.apps.blog',
    'proyectoinfo.apps.users',
    'proyectoinfo.apps.centros',
    #'geoposition',
    'crispy_forms',
    'import_export',
    'ckeditor',
    'location_field.apps.DefaultConfig',
]

LOCATION_FIELD = {
    'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    'provider.google.api_key': 'AIzaSyCNxnKZiPG95WmAcgEC1B4wZKw5IMwoi6g',
    'provider.google.api_libraries': '',
    'provider.google.map.type': 'ROADMAP',
    'map.zoom': 1,
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyectoinfo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'proyectoinfo/templates')],
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

WSGI_APPLICATION = 'proyectoinfo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT= os.path.join(BASE_DIR,'proyectoinfo/static/')

STATIC_URL = '/static/'
STATICFILES_DIRS =  (os.path.join(os.path.dirname(BASE_DIR), 'proyectoinfo/static'),)
#STATICFILES_DIRS =  (os.path.join(BASE_DIR, 'static/'),)
print('STATICFILES_DIRS: ', STATICFILES_DIRS)
#STATICFILES_DIRS = [ BASE_DIR / "static",  '/static/',]
MEDIA_URL = '/media/'
MEDIA_ROOT =  (os.path.join(os.path.dirname(BASE_DIR), 'proyectoinfo/media'),)

#lo que sigue es para cuando esta alojado en el server
"""

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/plasma-info/www/proyectoinfo/proyectoinfo/proyectoinfo/static/'
MEDIA_ROOT =  '/home/plasma-info/www/proyectoinfo/proyectoinfo/proyectoinfo/media/'
STATICFILES_DIRS = (
    '/home/plasma-info/www/proyectoinfo/proyectoinfo/proyectoinfo/static/',
)
"""

from django.urls import reverse_lazy
#from ..apps.users.models import Usuario

AUTH_USER_MODEL = "users.Usuario"

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('')

#smtp config

#Outgoing SMTP server: smtp-plasma-info.alwaysdata.net

