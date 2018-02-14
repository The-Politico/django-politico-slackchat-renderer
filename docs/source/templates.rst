Developing templates
====================

As long as your template files follow a few naming conventions, slackchat-renderer will be able to find them and use them to render a serialized slackchat.

Create your :code:`ChatType` instance in slackchat-serializer with a name which is a lowercase slug. You'll then use that slug to create the files that makeup your template.

By default, the render will look for each of these four template files when rendering a slackchat:

.. code::

  chatrender/
    templates/
      chatrender/
        <slug>/
          index.html
    static/
      chatrender/
        css/
          main-<slug>.css
        js/
          main-<slug>.js
          main-<slug>.js.map

This app includes our `webpack-based bundler <https://github.com/The-Politico/generator-politico-django>`_ to help compile your static files, so if you're developing template static files in :code:`staticapp` directory, you might organize your directory like this:

.. code::

  staticapp/
    src/
      js/
        main-<slug>.jsx
        <slug>/
          component.jsx
          # etc.
      scss/
        <slug>/
          styles.scss
          _partial.scss
          # etc.
