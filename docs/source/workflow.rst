Workflow
========

In general, here's the workflow when the app responds to a webhook from slackchat-serializer.

1. slackchat-serializer hits the app's endpoint with the ID of the channel which was updated.
2. The app makes a GET request to the channel's API URL and retrieves the serialized slackchat.
3. The app uses the serialized :code:`chat_type` to fetch the correct template files used to render the slackchat.
4. The app renders the template using the serialized slackchat as context.
5. The rendered slackchat is published to the S3 bucket at the location indicated by the serialized :code:`publish_path`.
