"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
import os

from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', x)
from oscar import get_core_apps
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR + '/media/'
STATIC_ROOT = BASE_DIR + '/static/'
MEDIA_URL = '/media/' 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'na2+sbbiap)(hg%grnn%iv*4+zq3q8uh&%35lq5f*pp&1@9*f1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['localhost','thelightened.gq','140.118.9.169','127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', #django sites framework
    'cafe',
    'tinymce',
    # 'sorl.thumbnail',
    'mce_filebrowser',
    'django_markdown',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'django.contrib.flatpages',
    'widget_tweaks',
    'adminrestrict', 
    'compressor',
    # 'paypal',
    # 'djangosecure',
    # 'sslserver',
] + get_core_apps()


# MailGun
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'succowork@gmail.com'
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = 'key-ecda648dbaaebda1966ec529ba1c98be'
MAILGUN_SERVER_NAME = 'thelightened.gq'
ACCOUNT_ACTIVATION_DAYS = 7
SITE_ID = 3


# LOGIN_REDIRECT_URL = "/index"

# Oscar
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending':('Being processed','Cancelled',),
    'Being processed':('processed','Cancelled',),
    'Cancelled':(),
}

OSCAR_SHOP_NAME = 'thelightened'
OSCAR_SHOP_TAGLINE = 'thelightened'
OSCAR_FROM_EMAIL = 'succowork@gmail.com'
OSCAR_DEFAULT_CURRENCY = 'TWD'


PAYPAL_API_USERNAME = 'tom20314-facilitator_api1.gmail.com'
PAYPAL_API_PASSWORD = 'N2F42W7J9EP5NKWR'
PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AmsacHUYUY3jX8S7Nnio-KsKWpiF'

PAYPAL_SANDBOX_MODE = True
PAYPAL_CURRENCY = 'TWD'
PAYPAL_BRAND_NAME = 'My SHOP'
PAYPAL_CALLBACK_HTTPS=False




HAYSTACK_CONNECTIONS = {
    'default':{
        'ENGINE':'haystack.backends.simple_backend.SimpleEngine',
    },
}

MIDDLEWARE_CLASSES = [
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
    'django.middleware.security.SecurityMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', 
    #adminrestrction
    # 'adminrestrict.middleware.AdminPagesRestrictMiddleware',
    #Security
    # 'djangosecure.middleware.SecurityMiddleware'
]

#secure
# SECURE_SSL_REDIRECT = True


ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # location('templates'),
            OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                 # allauth` needs this from django
                'django.template.context_processors.request',
                #oscar
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',                  
            ],
        },
    },
]



# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


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

#allauth
#after verification then login
ACCOUNT_EMAIL_VERIFICATION = "mandatory"


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
    'oscar.apps.customer.auth_backends.EmailBackend',
)




ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"
LOGIN_URL = "allauth/login"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT =3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =30
#unfixed


ACCOUNT_FORMS = {'allauth/login': 'cafe.forms.LoginForm'}
ACCOUNT_LOGIN_FORM_CLASS = 'cafe.forms.LogingForm'

ACCOUNT_FORMS = {'allauth/signup': 'cafe.forms.SignupForm'}
ACCOUNT_SIGNUP_FORM_CLASS= 'cafe.forms.SignupForm'

ACCOUNT_LOGOUT_REDIRECT_URL ='/index'



#Mail
ACCOUNT_EMAIL_CONFIRMATION_HMAC =True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =False
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQURIED=True
ACCOUNT_UNIQUE_EMAIL =False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'index'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL ='/accounts/profile'
# LOGIN_REDIRECT_URL = "/index"