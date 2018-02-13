"""
Use this file to configure pluggable app settings and resolve defaults
with any overrides set in project settings.
"""
import re

from django.conf import settings as project_settings


class Settings:
    pass


Settings.WEBHOOK_VERIFICATION_TOKEN = getattr(
    project_settings,
    'CHATRENDER_WEBHOOK_VERIFICATION_TOKEN',
    'slackchat'
)

Settings.SLACKCHAT_CHANNEL_ENDPOINT = getattr(
    project_settings,
    'CHATRENDER_SLACKCHAT_CHANNEL_ENDPOINT',
    None
)

Settings.DEV_SLACKCHAT_CHANNEL_ENDPOINT = getattr(
    project_settings,
    'CHATRENDER_DEV_SLACKCHAT_CHANNEL_ENDPOINT',
    None
)

# Strip leading slash, if necessary...
Settings.AWS_S3_PUBLISH_PATH = re.sub(r'^/', '', getattr(
    project_settings,
    'CHATRENDER_AWS_S3_PUBLISH_PATH',
    'slackchats/'
))

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

Settings.SECRET_KEY = getattr(
    project_settings, 'CHATRENDER_SECRET_KEY', 'a-bad-secret-key')

Settings.AWS_ACCESS_KEY_ID = getattr(
    project_settings, 'CHATRENDER_AWS_ACCESS_KEY_ID', None)

Settings.AWS_SECRET_ACCESS_KEY = getattr(
    project_settings, 'CHATRENDER_AWS_SECRET_ACCESS_KEY', None)

Settings.AWS_REGION = getattr(
    project_settings, 'CHATRENDER_AWS_REGION', 'us-east-1')

Settings.AWS_S3_BUCKET = getattr(
    project_settings, 'CHATRENDER_AWS_S3_BUCKET', None)


settings = Settings
