from django.urls import path

from .views import Endpoint, channel, develop

urlpatterns = [
    path('endpoint/', Endpoint.as_view()),
    path(
        'develop/<slug:chat_type>/<slug:channel>/',
        develop,
        name="chatrender-channel"
    ),
    path('<slug:chat_type>/channels/', channel),
]
