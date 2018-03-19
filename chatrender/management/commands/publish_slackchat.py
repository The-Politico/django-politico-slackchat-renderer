from chatrender.celery import publish_slackchat
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Publishes a complete slackchat package, including static files.'

    def add_arguments(self, parser):
        parser.add_argument('--type', dest='chat_type')
        parser.add_argument('--channel', dest='channel')

    def handle(self, *args, **options):
        chat_type = options.get('chat_type')
        channel = options.get('channel')
        if not chat_type or not channel:
            raise CommandError('You must specify a channel ID and chat type.')

        publish_slackchat.delay(
            chat_type,
            channel,
            statics=True
        )

        print('Done.')
