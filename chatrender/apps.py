from django.apps import AppConfig


class ChatrenderConfig(AppConfig):
    name = 'chatrender'

    def ready(self):
        from chatrender import signals  # noqa
