from urllib.parse import urljoin

import requests

from chatrender.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


@staff_member_required
def develop(request, chat_type, channel):
    channel_uri = urljoin(settings.SLACKCHAT_CHANNEL_ENDPOINT, channel)
    response = requests.get(channel_uri)

    channel = response.json()
    return render(
        request,
        'chatrender/{}/index.html'.format(chat_type),
        context={
            "channel": channel,
            "channel_uri": channel_uri,
            "origin": settings.AWS_CUSTOM_ORIGIN,
            "publish_path": settings.AWS_S3_PUBLISH_PATH,
            "develop": True,
        }
    )
