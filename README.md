# Coffee App Backend

This repo contains the backend code for Coffee Project's app. It provides
an API call that allows the app to retrieve data about cafés, and it allows
you to use the Django admin interface to manage the data.

## Running a development server

You can install the module by cloning the repo and running
`pip3 install --user --editable .` inside it.

To run a development server,  run `django-admin startproject mysite` to create
a new project. Then:

1. Add "coffeeapp\_backend" to the `INSTALLED_APPS` list in `mysite/settings.py`.

2. Add `url(r'^polls/', include('polls.urls')),` to the list of URLs in your project's `urls.py`.

3. Run `python3 manage.py migrate` to create the models.

4. Start the development server using `python3 manage.py runserver`.

[django-install]: https://docs.djangoproject.com/en/2.0/topics/install/

## Contributing

Before committing code to the repo, please run [Black][] on it.

[black]: https://github.com/ambv/black
