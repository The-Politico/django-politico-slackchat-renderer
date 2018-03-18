from django.urls import path

from .views import Channel, Endpoint, channels, chat_types

urlpatterns = [
    path('endpoint/', Endpoint.as_view()),
    path(
        'develop/<slug:chat_type>/<slug:channel_id>/',
        Channel.as_view(),
        name="chatrender_channel"
    ),
    path('<slug:chat_type>/channels/', channels, name="chatrender_channels"),
    path('', chat_types, name="chatrender_home")
]
