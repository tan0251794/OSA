
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2&qybcjq!t7rhknwr$4t!5cm94@)x5wc2_w!m+(if%irm0^j@3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['osa-api.herokuapp.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'purchase_app',
    'accounts',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'OSA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'OSA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#postgres://ueupixppedfzad:a323b5463df62956a3ab468c73cf6c17952355a48060cb928ad7ae140f05e6bc@ec2-44-198-154-255.compute-1.amazonaws.com:5432/dtruv7pql1dru
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dtruv7pql1dru',
        'HOST': 'ec2-44-198-154-255.compute-1.amazonaws.com',
        'POST': 5432,
        'USER': 'ueupixppedfzad',
        'PASSWORD': 'a323b5463df62956a3ab468c73cf6c17952355a48060cb928ad7ae140f05e6bc',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        #
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  
        'drf_social_oauth2.authentication.SocialAuthentication',
    ]
}

AUTH_USER_MODEL = 'accounts.UserAccounts'

LOGIN_REDIRECT_URL ="../order/"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    #drf
    'social_core.backends.google.GoogleOAuth2', 
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SITE_ID = 3

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "908666684854-09u78tmd7jpfksanfmabs1dgvft4dcud.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"
# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
   'https://www.googleapis.com/auth/userinfo.email',
   'https://www.googleapis.com/auth/userinfo.profile',
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ['*']


