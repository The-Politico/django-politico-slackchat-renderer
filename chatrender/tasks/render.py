import gc
import json
import logging
import os
from urllib.parse import urljoin
from urllib.request import urlopen

import requests

from celery import shared_task
from chatrender.conf import settings
from chatrender.exceptions import (ChannelNotFoundError,
                                   StaticFileNotFoundError,
                                   TemplateNotFoundError)
from chatrender.utils.aws import check_object_exists, defaults, get_bucket
from chatrender.utils.path import relativize_path
from django.conf import settings as project_settings
from django.contrib.sites.models import Site
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


def render_local_static(static_file):
    """Render local static file to string to inject into template."""
    URI = os.path.join(
        Site.objects.get_current().domain,
        relativize_path(static(static_file))
    )
    try:
        protocol = 'http' if project_settings.DEBUG else 'https'
        return urlopen(
            '{0}://{1}'.format(protocol, URI)
        ).read().decode('UTF-8')
    except Exception:
        raise StaticFileNotFoundError(
            'Could not connect to find staticfile: {}. \
            \nAre you sure you have the right domain configured \
            in Django sites framework?'.format(static_file))


def publish_slackchat(channel, statics=False):
    """
    Publishes data and static assets associated with a template to
    the publish path set in django slackchat.
    """
    publish_path = relativize_path(channel.get('publish_path'))
    chat_type = channel.get('chat_type')

    bucket = get_bucket()

    try:
        rendered_chat = render_to_string(
            'chatrender/{}/index.html'.format(chat_type),
            {
                "channel": channel,
                "origin": settings.AWS_CUSTOM_ORIGIN,
                "publish_path": settings.AWS_S3_PUBLISH_PATH,
                "develop": False,
            }
        )
    except TemplateDoesNotExist:
        raise TemplateNotFoundError(
            'Could not find template for chat type: {}'.format(chat_type))

    # index.html
    key = os.path.join(
        settings.AWS_S3_PUBLISH_PATH,
        publish_path,
        'index.html'
    )

    bucket.put_object(
        Key=key,
        ACL=defaults.ACL,
        Body=rendered_chat,
        CacheControl=str('max-age=60'),
        ContentType='text/html'
    )

    # chat.json
    key = os.path.join(
        settings.AWS_S3_PUBLISH_PATH,
        publish_path,
        'chat.json'
    )

    bucket.put_object(
        Key=key,
        ACL=defaults.ACL,
        Body=json.dumps(channel),
        CacheControl=str('max-age=5'),
        ContentType='application/json'
    )

    if statics:
        # main-{}.js
        rendered_js = render_local_static(
            'chatrender/js/main-{}.js'.format(chat_type))

        key = os.path.join(
            settings.AWS_S3_PUBLISH_PATH,
            publish_path,
            'main-{}.js'.format(chat_type)
        )

        bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=rendered_js,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='application/javascript'
        )

        # main-{}.js.map
        rendered_js = render_local_static(
            'chatrender/js/main-{}.js.map'.format(chat_type))

        key = os.path.join(
            settings.AWS_S3_PUBLISH_PATH,
            publish_path,
            'main-{}.js.map'.format(chat_type)
        )

        bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=rendered_js,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='application/octet-stream'
        )

        # main-{}.css
        rendered_css = render_local_static(
            'chatrender/css/main-{}.css'.format(chat_type))

        key = os.path.join(
            settings.AWS_S3_PUBLISH_PATH,
            publish_path,
            'main-{}.css'.format(chat_type)
        )

        bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=rendered_css,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='text/css'
        )


@shared_task(acks_late=True)
def render_slackchat(channel_id):
    channel_uri = urljoin(settings.SLACKCHAT_CHANNEL_ENDPOINT, channel_id)
    response = requests.get(channel_uri)

    if response.status_code != 200:
        raise ChannelNotFoundError(
            'Could not find channel at: {}'.format(channel_uri))

    channel = response.json()
    publish_path = relativize_path(channel.get('publish_path'))

    key = os.path.join(
        settings.AWS_S3_PUBLISH_PATH,
        publish_path,
        'index.html'
    )

    # Don't republish static assets if they exist already at this location.
    # If you NEED to republish assets, use the management command.
    if not check_object_exists(key):
        publish_slackchat(channel, statics=True)
    else:
        publish_slackchat(channel, statics=False)

    logger.info('Published slckchat to AWS.')
    # Garbage collect after run.
    gc.collect()
