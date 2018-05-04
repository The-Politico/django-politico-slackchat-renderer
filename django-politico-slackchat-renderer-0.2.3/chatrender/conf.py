"""
Use this file to configure pluggable app settings and resolve defaults
with any overrides set in project settings.
"""
from urllib.parse import urljoin

from django.conf import settings as project_settings


class Settings:
    pass


Settings.WEBHOOK_VERIFICATION_TOKEN = getattr(
    project_settings,
    'CHATRENDER_WEBHOOK_VERIFICATION_TOKEN',
    'slackchat'
)


Settings.SLACKCHAT_API_ENDPOINT = getattr(
    project_settings,
    'CHATRENDER_SLACKCHAT_API_ENDPOINT',
    None
)

Settings.SLACKCHAT_CHANNEL_ENDPOINT = urljoin(
    Settings.SLACKCHAT_API_ENDPOINT,
    'channels/'
)

Settings.SLACKCHAT_CHATTYPE_ENDPOINT = urljoin(
    Settings.SLACKCHAT_API_ENDPOINT,
    'chat-types/'
)

# Strip leading slash, if necessary...
Settings.AWS_S3_PUBLISH_PATH = getattr(
    project_settings,
    'CHATRENDER_AWS_S3_PUBLISH_PATH',
    ''
).lstrip('/')

Settings.AWS_CUSTOM_ORIGIN = getattr(
    project_settings,
    'CHATRENDER_AWS_CUSTOM_ORIGIN',
    None
)

Settings.AUTH_DECORATOR = getattr(
    project_settings,
    'CHATRENDER_AUTH_DECORATOR',
    'django.contrib.auth.decorators.login_required'
)

Settings.AWS_ACCESS_KEY_ID = getattr(
    project_settings, 'CHATRENDER_AWS_ACCESS_KEY_ID', None)

Settings.AWS_SECRET_ACCESS_KEY = getattr(
    project_settings, 'CHATRENDER_AWS_SECRET_ACCESS_KEY', None)

Settings.AWS_REGION = getattr(
    project_settings, 'CHATRENDER_AWS_REGION', 'us-east-1')

Settings.AWS_S3_BUCKET = getattr(
    project_settings, 'CHATRENDER_AWS_S3_BUCKET', None)

Settings.AWS_CLOUDFRONT_DISTRIBUTION = getattr(
    project_settings, 'CHATRENDER_AWS_CLOUDFRONT_DISTRIBUTION', None)


settings = Settings
