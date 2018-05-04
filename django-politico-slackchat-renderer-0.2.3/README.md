![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-slackchat-renderer

Pair app to [django-slackchat-serializer](https://github.com/The-Politico/django-slackchat-serializer). By their powers combined, we publish SlackChats.

[Read the docs](http://django-politico-slackchat-renderer.readthedocs.io/en/latest/index.html).


## Developing for Designers

#### What you'll need:

- Two open terminals
- Slack
- Your browser

### Steps

#### Setup

1. Make sure your `/example/.env` is filled out with these variables:

  ```
  SLACK_VERIFICATION_TOKEN="<token>"
  SLACK_API_TOKEN="<token>"
  AWS_ACCESS_KEY_ID="<id>"
  AWS_SECRET_ACCESS_KEY="<key>"
  AWS_S3_BUCKET="staging.interactives.politico.com"
  ```
2. Open terminal to `example/` directory and install dependencies:

  ```
  $ cd example
  $ pipenv install
  ```
3. Change to `chatrender/staticapp`, install dependencies and run Gulp:

  ```
  $ cd ../chatrender/staticapp/
  $ yarn
  $ gulp
  ```
4. In your second terminal, start ngrok and proxy `localhost:3000`:

  ```
  $ ngrok http 3000
  ```
5. Copy the HTTPS proxy address from ngrok terminal:

  ```
  https://xyz123.ngrok.io
  ```
6. Update the Slack app.
  1. Visit https://api.slack.com/apps and click through to the `SlackChatApp`.
  2. Under `Features`, click `Event Subscriptions`.
  3. In the `Enable Events` section, update the `Request URL` with the HTTPS address you copied from ngrok but add `/slackchat/events/` to the path, e.g., `https://xyz123.ngrok.io/slackchat/events/`.
  4. Once you add the address, Slack should automatically verify the URL. If it doesn't, ask a developer for help.

#### Templates

Remember, every template must have a corresponding chat_type in the Django admin. Copy the structure from a previous template to start building a new one.
