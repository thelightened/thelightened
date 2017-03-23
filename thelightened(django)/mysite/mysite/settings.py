"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR + '/media/'
MEDIA_URL = '/media/' 
# STATICFILES_DIR = (os.path.join(BASE_DIR, 'static'),)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-b$3o)&k19l&)2*itm9ed)(4*f!+y)+gq)dlqx6u+!rlj%h*ez'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = "account/"
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites', #django sites framework
    'cafe',
    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    'django_markdown',
    'registration', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
	# 'google_analytics',


)

EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'succowork@gmail.com'
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = 'key-ecda648dbaaebda1966ec529ba1c98be'
MAILGUN_SERVER_NAME = 'thelightened.gq'
ACCOUNT_ACTIVATION_DAYS = 7
SITE_ID = 3


# facebook social
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQURIED=True
LOGIN_REDIRECT_URL = "/index"


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# mysql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'thelighteneddb',  
#         'USER': 'root',  
#         'PASSWORD': 'admin',   
#         'HOST': '',  
#         'PORT': '',   
#     }
# }



# sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# GOOGLE_ANALYTICS_MODEL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


TINYMCE_DEFAULT_CONFIG = {
  'file_browser_callback': 'mce_filebrowser'
}

# facebook test

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}}

#facebook
SOCIAL_AUTH_FACEBOOK_KEY = '101197950365729'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET ='a32dd33e7590fa655d211903e6d00e4b' #app key