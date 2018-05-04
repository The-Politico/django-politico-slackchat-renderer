import requests

from chatrender.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


@staff_member_required
def channels(request, chat_type):
    response = requests.get('{}?chat_type={}'.format(
        settings.SLACKCHAT_CHANNEL_ENDPOINT,
        chat_type,
    ))
    channels = response.json()
    return render(
        request,
        'chatrender/channel_list.html',
        context={"channels": channels, "chat_type": chat_type}
    )
