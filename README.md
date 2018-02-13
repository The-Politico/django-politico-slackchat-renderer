![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-politico-slackchat-renderer

### Quickstart

1. Install the app.

  ```
  $ pip install django-politico-slackchat-renderer
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'chatrender',
  ]

  def markslack_user_template(user):
      return '<span class="mention">{}</span>'.format(
          user.first_name
      )


  SLACKCHAT_SLACK_VERIFICATION_TOKEN = os.getenv(
      'SLACK_VERIFICATION_TOKEN', None)
  SLACKCHAT_SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN', None)
  SLACKCHAT_PUBLISH_ROOT = 'https://www.politico.com/interactives/slackchats/'
  SLACK_MARKSLACK_USER_TEMPLATE = markslack_user_template


  CHATRENDER_AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
  CHATRENDER_AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
  CHATRENDER_AWS_S3_BUCKET = 'interactives.politico.com'
  CHATRENDER_AWS_S3_PUBLISH_PATH = '/interactives/slackchats/'
  CHATRENDER_AWS_CUSTOM_ORIGIN = 'https://www.politico.com/interactives/'
  CHATRENDER_SLACKCHAT_CHANNEL_ENDPOINT = (
      'http://localhost:8000/slackchat/api/channels/'
  )
  CHATRENDER_DEV_SLACKCHAT_CHANNEL_ENDPOINT = (
      'http://80d94f62.ngrok.io/slackchat/api/channels/'
  )
  ```

### Developing

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```

Developing static assets? Move into the pluggable app's staticapp directory and start the node development server, which will automatically proxy Django's development server.

  ```
  $ cd chatrender/staticapp
  $ gulp
  ```

Want to not worry about it? Use the shortcut make command.

  ```
  $ make dev
  ```

##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to the `.env` file.

  ```
  DATABASE_URL="postgres://localhost:5432/chatrender"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```
