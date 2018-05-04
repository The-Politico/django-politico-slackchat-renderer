import requests

from chatrender.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


@staff_member_required
def chat_types(request):
    response = requests.get(settings.SLACKCHAT_CHATTYPE_ENDPOINT)
    context = response.json()
    return render(
        request,
        'chatrender/chattype_list.html',
        context={"chat_types": context}
    )
