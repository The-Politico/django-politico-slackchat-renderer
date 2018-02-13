import requests

from chatrender.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


@staff_member_required
def channel(request, chat_type):
    response = requests.get(settings.SLACKCHAT_CHANNEL_ENDPOINT)
    context = response.json()
    return render(
        request,
        'chatrender/channel_list.html',
        context={"channels": context, "chat_type": chat_type}
    )
