# Decoupled Django

This repository follows along Valentino Gagliardi's Decoupled Django [book](https://www.amazon.com/Decoupled-Django-Valentino-Gagliardi/dp/1484271432), originally published in 2021. You can find his
source code [here](https://github.com/valentinogagliardi/decoupled-dj).

There are two applications that are worked on, a billing application and a blog. Each of these apps
will show how to connect different JavaScript frontend frameworks, such as React and Vue to Django 
and it's REST framework.
 
This repository uses [Poetry](https://python-poetry.org/) for dependency management. To get started, 
download Poetry, then from your command line run:

```console
uname@os:~$ poetry shell
uname@os:~$ poetry install
```

Once the dependencies are updated, you need to setup your enviornment variables and configure the 
project settings to match our development file. Run:

```console
uname@os:~$ export DJANGO_SETTINGS_MODULE=decoupled_dj.settings.development
```

Now that the settings are configured, run the project by migrating the database and 
running the ASGI Uvicorn server.

```console
uname@os:~$ python manage.py makemigrations
uname@os:~$ python manage.py migrate
uname@os:~$ python manage.py collectstatic
uname@os:~$ python manage.py runserver
```