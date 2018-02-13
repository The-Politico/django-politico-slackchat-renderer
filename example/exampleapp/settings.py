import os

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET')

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework_swagger',
    'slackchat',
    'chatrender',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'exampleapp.urls'

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

WSGI_APPLICATION = 'exampleapp.wsgi.application'


DATABASES = {}
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 20,
        }
    }


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

SITE_ID = 1

#########################
# chatrender settings

CORS_ORIGIN_ALLOW_ALL = True

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


def markslack_user_template(user):
    return '<span class="mention">{}</span>'.format(
        user.first_name
    )


SLACKCHAT_SLACK_VERIFICATION_TOKEN = os.getenv(
    'SLACK_VERIFICATION_TOKEN', None)
SLACKCHAT_SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN', None)
SLACKCHAT_PUBLISH_ROOT = 'https://www.politico.com/interactives/slackchats/'
SLACK_MARKSLACK_USER_TEMPLATE = markslack_user_template


CHATRENDER_AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
CHATRENDER_AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
CHATRENDER_AWS_S3_BUCKET = 'interactives.politico.com'
CHATRENDER_AWS_S3_PUBLISH_PATH = '/interactives/slackchats/'
CHATRENDER_AWS_CUSTOM_ORIGIN = 'https://www.politico.com/interactives/'
CHATRENDER_SLACKCHAT_CHANNEL_ENDPOINT = (
    'http://localhost:8000/slackchat/api/channels/'
)
CHATRENDER_DEV_SLACKCHAT_CHANNEL_ENDPOINT = (
    'http://80d94f62.ngrok.io/slackchat/api/channels/'
)
