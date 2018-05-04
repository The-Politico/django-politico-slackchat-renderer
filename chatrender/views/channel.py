import json
import logging
import os
import uuid
from datetime import datetime
from urllib.parse import urljoin

import requests

from chatrender.conf import settings
from chatrender.exceptions import ChannelNotFoundError, StaticFileNotFoundError
from chatrender.utils.aws import (check_object_exists, defaults, get_bucket,
                                  get_cloudfront_client)
from django.conf import settings as project_settings
from django.test.client import RequestFactory
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


class Channel(TemplateView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bucket = get_bucket()
        self.hash = uuid.uuid4().hex[:10]

    def get_template_names(self):
        template = 'chatrender/{}/index.html'.format(self.chat_type)
        return (template,)

    def get_publish_path(self):
        return os.path.join(
            settings.AWS_S3_PUBLISH_PATH,
            self.channel['publish_path'].lstrip('/'),
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.chat_type = context['chat_type'] = self.kwargs.get('chat_type')
        self.channel_id = context['channel_id'] = self.kwargs.get('channel_id')
        self.channel_uri = context['channel_uri'] = urljoin(
            settings.SLACKCHAT_CHANNEL_ENDPOINT,
            self.channel_id
        )
        self.channel = context['channel'] = self.get_channel()
        context['origin'] = settings.AWS_CUSTOM_ORIGIN
        context['publish_path'] = self.get_publish_path()
        context['production'] = self.request.GET.get('env', 'dev') == 'prod'
        context['hash'] = self.hash
        context['now'] = datetime.now()
        return context

    def get_channel(self):
        response = requests.get(self.channel_uri)

        if response.status_code != 200:
            raise ChannelNotFoundError(
                'Could not find channel at: {}'.format(self.channel_uri))
        return response.json()

    @staticmethod
    def render_static_string(path):
        """Renders static file to string.

        Must have run collectstatic first.
        """
        absolute_path = os.path.join(
            project_settings.STATIC_ROOT,
            path
        )
        try:
            with open(absolute_path, 'rb') as staticfile:
                return staticfile.read()
        except (OSError, IOError):
            raise StaticFileNotFoundError(
                'Couldn\'t find the file {}. Are you sure you '
                'have run collectstatic?'.format(path)
            )

    def publish_js(self):
        """Publishes JS bundle."""
        static_file = 'main-{}.js'.format(self.chat_type)
        static_file_path = 'chatrender/js/{}'.format(static_file)
        hashed_path = 'main-{}-{}.js'.format(self.chat_type, self.hash)
        js_string = self.render_static_string(static_file_path)
        key = os.path.join(
            self.get_publish_path(),
            hashed_path
        )
        logger.info('>>> Publish JS to:', key)
        self.bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=js_string,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='application/javascript'
        )
        # Maps
        map_string = self.render_static_string(
            '{}.map'.format(static_file_path)
        )
        key = os.path.join(
            self.get_publish_path(),
            '{}.map'.format(hashed_path)
        )
        logger.info('>>> Publish JS map to:', key)
        self.bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=map_string,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='application/octet-stream'
        )

    def publish_css(self):
        """Publishes CSS."""
        static_file = 'main-{}.css'.format(self.chat_type)
        static_file_path = 'chatrender/css/{}'.format(static_file)
        hashed_path = 'main-{}-{}.css'.format(self.chat_type, self.hash)
        css_string = self.render_static_string(static_file_path)
        key = os.path.join(
            self.get_publish_path(),
            hashed_path
        )
        logger.info('>>> Publish CSS to:', key)
        self.bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=css_string,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='text/css'
        )

    def get_request(self):
        """Construct a request we can use to render the view."""
        kwargs = {
            'chat_type': self.chat_type,
            'channel_id': self.channel_id,
            'env': 'prod',
        }
        return RequestFactory().get('', kwargs)

    def publish_template(self, **kwargs):
        request = self.get_request()
        view = self.__class__.as_view()(
            request, **kwargs)
        self.hash = view.context_data.get('hash')
        template_string = view.rendered_content
        key = os.path.join(
            self.get_publish_path(),
            'index.html'
        )
        logger.info('>>> Publish template to:', key)
        self.bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=template_string,
            CacheControl=defaults.CACHE_HEADER,
            ContentType='text/html'
        )

        cloudfront = get_cloudfront_client()
        if cloudfront:
            logger.info('>>> Invalidate template:', key)
            cloudfront.create_invalidation(
                DistributionId=settings.AWS_CLOUDFRONT_DISTRIBUTION,
                InvalidationBatch={
                    'Paths': {
                        'Quantity': 1,
                        'Items': [
                            '/{}'.format(key)
                        ]
                    },
                    'CallerReference': '{}'.format(datetime.now())
                }
            )

    def publish_serialized_chat(self):
        key = os.path.join(
            self.get_publish_path(),
            'chat.json'
        )
        logger.info('>>> Publish chat data to:', key)
        self.bucket.put_object(
            Key=key,
            ACL=defaults.ACL,
            Body=json.dumps(self.channel),
            CacheControl=str('max-age=5'),
            ContentType='application/json'
        )

    def publish(self, **kwargs):
        self.chat_type = kwargs.get('chat_type')
        self.channel_id = kwargs.get('channel_id')
        self.channel_uri = urljoin(
            settings.SLACKCHAT_CHANNEL_ENDPOINT,
            self.channel_id
        )
        self.channel = self.get_channel()
        self.publish_serialized_chat()

        # Publish statics explicitly or if not pub'd before
        index = os.path.join(self.get_publish_path(), 'index.html')
        if kwargs.get('statics') or not check_object_exists(index):
            self.publish_template(**kwargs)
            self.publish_js()
            self.publish_css()
