Stock Price Viewer
==================

This app views stock price histories retrieved from the Yahoo Finance API.

The backend is a Django application whose notable dependencies include:

* [Django REST Framework](http://www.django-rest-framework.org/): tools for
  building REST APIs in Django.
* [python-dateutil](http://labix.org/python-dateutil): improved
  date-manipulation tools for Python, expanding on the built-in `datetime`
  library.
* [yahoo-finance](https://github.com/lukaszbanasiak/yahoo-finance): Python
  wrapper for the Yahoo Finance HTTP API.

The frontend is written in Ember. In addition to Ember itself, it uses:

* [Bootstrap](http://getbootstrap.com/)
* [ember-django-adapter](http://dustinfarris.com/ember-django-adapter/): An
  Adapter/Serializer pair that configures Ember to use the default JSON output
  of Django REST Framework.
* [ember-moment](https://github.com/stefanpenner/ember-moment): An Ember wrapper
  around the [Moment.JS](http://momentjs.com/) date-manipulation library.
* [ember-cli-chart](https://github.com/aomra015/ember-cli-chart): An Ember
  component wrapper for [ChartJS](http://www.chartjs.org/)

Installing
----------

This project requires a unix-like environment with:

* Python 2.7+ and pip (the Python package manager). As of Python 2.7.9, pip is
  included with Python by default -- if you don't already have it, it should be
  available from your system's package manager.
* `virtualenvwrapper` for python, which is available from pip. To install
  `virtualenvwrapper`, run: `pip install virtualenvwrapper`. Depending on how
  Python was installed, this may require `sudo`.
* Node.JS 0.12.4 and npm (the Node package manager). Node and npm are always
  bundled together, and should be available from your system's package manager.

Once Python and Node are installed, follow these steps:

1. `cd` to the `server` directory of the repository.
2. `mkvirtualenv dough-coding-exercise` (this creates an isolated Python
   environment for project dependencies, and activates it).
3. `pip install -r requirements.txt`
4. `./manage.py migrate`
5. `./manage.py import_companies` (this imports companies as CSV data from the
   `server/companies` directory, with each file corresponding to one exchange --
   you can load files from a different directory by specifying the `--csvdir`
   option.
6. `cd` to the `client` directory of the repository.
7. `npm install`
8. `bower install`


Running the Project
-------------------

In one terminal:

1. `cd` to the `server` directory of the repository.
2. `workon dough-coding-exercise`
3. `./manage.py runserver`

In another terminal:

1. `cd` to the `client` directory of the repository.
2. `ember s`

The app will be accessible at http://localhost:4200


Notes
-----

* The search bar at the top of the page will search for companies by name or
  symbol.
* Queries for price history are **cached on the client side** using an Ember
  service backed by localStorage, with a one-day timeout. Note that repeated
  visits to the same company URL do not provoke additional requests against
  /api/companies/:id/price-history
