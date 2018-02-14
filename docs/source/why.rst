Why this?
=========

Pairs with `django-slackchat-serializer <http://django-slackchat-serializer.readthedocs.io/en/latest/index.html>`_, an app that serializes conversations within a Slack channel and fires webhooks whenever new messages are added.

This app responds to slackchat-serializer's webhooks and publishes the serialized data within a template. It maintains no data, itself, and therefore has no models, but is the repository of the templates used at POLITICO to render serialized SlackChats. It also includes the logic we use to publish SlackChats as static files to an AWS S3 bucket.

.. note::

  We've open-sourced this project mostly to serve as an example of how we interact with `django-slackchat-serializer <http://django-slackchat-serializer.readthedocs.io/en/latest/index.html>`_.

  That said, this project may not be wholly useful on its own to folks outside our team. In fact, a major part of the app is maintaining our branded templates. But if you're looking to follow our lead when rendering serialized slackchats, we encourage you to check out the `source code <https://github.com/The-Politico/django-politico-slackchat-renderer>`_ in conjunction with these (admittedly sparse) docs.
