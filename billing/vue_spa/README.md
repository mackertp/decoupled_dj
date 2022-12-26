# vue SPA

This is an example of a decoupled *Single Page Application* using javascript's vue framework. 
The application is a simple application to create invoices.

To get started, you will need to have [Vue CLI](https://cli.vuejs.org/) installed. You can then
install the dependencies and lint your code with [yarn](https://yarnpkg.com/).

```console
uname@os:~$ yarn install
uname@os:~$ yarn lint

Once the dependencies are installed, there are two ways to run this application. You can run the
application using Vue's development server from this directory:

```console
uname@os:~$ yarn serve
```

Or you can build the app from this directory:

```console
uname@os:~$ yarn build --mode staging
```

Then from the Django project root, run:

```console
uname@os:~$ python manage.py collectstatic
uname@os:~$ python manage.py runserver
```

This allows you to see the full django project working as you would expect. Navigating to
http://127.0.0.1:8000/billing/ will load the Vue application.
