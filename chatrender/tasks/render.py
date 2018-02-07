import logging
import os
import re
from urllib.parse import urljoin

import requests

from celery import shared_task
from chatrender.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import render_to_string

# from chatrender.utils.aws import defaults, get_bucket

logger = logging.getLogger('tasks')

CHANNEL_API_URI = urljoin(settings.SERIALIZER_API_URL, 'channel/')


def relativize_path(path):
    return re.sub('^/', '', path)


def render_local_static(static_file):
    """Render local static file to string to inject into template."""
    return requests.get(
        os.path.join(
            'A DOMAIN',
            static(static_file)[1:]
        )
    ).text


@shared_task(acks_late=True)
def render_slackchat(id):
    channel_uri = urljoin(CHANNEL_API_URI, id)
    response = requests.get(channel_uri)
    data = response.json()

    publish_path = relativize_path(data.get('publish_path'))

    template_type = data.get('chat_type')
    print(template_type)

    key = os.path.join(
        settings.AWS_PUBLISH_ROOT,
        publish_path,
        'data.json'
    )
    print(key)
    # bucket = get_bucket()
    #
    # bucket.put_object(
    #     Key=key,
    #     ACL=defaults.ACL,
    #     Body='{}',
    #     CacheControl=defaults.CACHE_HEADER,
    #     ContentType='application/json'
    # )
    #
    # logger.info('Published to AWS')
