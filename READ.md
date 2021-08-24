Flaskr
======

Neuro test case for find specific location distance from Moscow Ring Road.



Install
-------

    # clone the repository
    $ git clone https://github.com/berkaykrc/neuro-case
    $ cd neuro-case

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install neuro-case::

    $ pip install -e .


Run
---

::

    $ export FLASK_APP=neuro-case
    $ export CONFIGURATION_SETUP=config.DevelopmentConfig
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=flaskr
    > set FLASK_ENV=development
    > flask init-db
    > flask run

Open http://127.0.0.1:5000 in a browser.


Test
----

::

    $ pip install pytest coverage
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser