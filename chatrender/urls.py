from django.urls import path

from .views import Endpoint, channel, chattype, develop

urlpatterns = [
    path('endpoint/', Endpoint.as_view()),
    path(
        'develop/<slug:chat_type>/<slug:channel>/',
        develop,
        name="chatrender_channel"
    ),
    path('<slug:chat_type>/channels/', channel, name="chatrender_channels"),
    path('', chattype, name="chatrender_home")
]
