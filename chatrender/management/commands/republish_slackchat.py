from urllib.parse import urljoin

import requests

from chatrender.conf import settings
from chatrender.tasks.render import publish_slackchat
from django.core.management.base import BaseCommand, CommandError
from slackchat.models import Channel


class Command(BaseCommand):
    help = 'Publishes a complete slackchat package, including static files.'

    def add_arguments(self, parser):
        parser.add_argument('api_id', nargs='+')

    def handle(self, *args, **options):
        for api_id in options['api_id']:
            channel = Channel.objects.get(api_id=api_id)
            channel_uri = urljoin(
                settings.SLACKCHAT_CHANNEL_ENDPOINT, channel.id.hex)
            response = requests.get(channel_uri)

            if response.status_code != 200:
                raise CommandError(
                    'Could not find channel at: {}'.format(channel_uri))

            channel = response.json()

            print('> Publishing "{}"'.format(channel.get('title')))

            publish_slackchat(channel, statics=True)

        print('Done.')
