Quickstart
==========

1. Install the app:

  .. code::

    $ pip install django-politico-slackchat-renderer

2. Add the app to your installed apps and your project's urls.py.

  .. code-block:: python

    # project/settings.py

    INSTALLED_APPS = [
        # ...
        'chatrender',
    ]


  .. code-block:: python

    # project/urls.py

    urlpatterns = [
        # ...
        path('chatrender', include('chatrender.urls')),
    ]

3. Configure settings.

  .. code-block:: python

    # project/settings.py

    # AWS credentials and S3 bucket
    CHATRENDER_AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    CHATRENDER_AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    CHATRENDER_AWS_S3_BUCKET = 'interactives.politico.com'

    # Root path in bucket for publishing slackchats
    CHATRENDER_AWS_S3_PUBLISH_PATH = '/interactives/slackchats/'

    # The URL root the bucket is proxied to
    CHATRENDER_AWS_CUSTOM_ORIGIN = 'https://www.politico.com/interactives/'

    # slackchat-serializers root API URL
    CHATRENDER_SLACKCHAT_API_ENDPOINT = 'http://localhost:8000/slackchat/api/'

4. In django-slackchat-serializer, create a :code:`ChatType` instance whose slug matches a renderer template name (cf. Developing) and configure a webhook to hit the events endpoint at :code:`<chatrender>/endpoint/`.
