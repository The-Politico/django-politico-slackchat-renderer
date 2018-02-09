from urllib.parse import urljoin

import requests

from django.core.management.base import BaseCommand, CommandError
from slackchat.conf import settings
from slackchat.tasks.render import publish_slackchat


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('channel_id', nargs='+')

    def handle(self, *args, **options):
        for channel_id in options['channel_id']:
            channel_uri = urljoin(
                settings.SLACKCHAT_CHANNEL_ENDPOINT, channel_id)
            response = requests.get(channel_uri)

            if response.status_code != 200:
                raise CommandError(
                    'Could not find channel at: {}'.format(channel_uri))

            channel = response.json()

            print('> Publishing "{}"'.format(channel.get('title')))

            publish_slackchat(channel, statics=True)

        print('Done.')
