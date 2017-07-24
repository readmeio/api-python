
This is a language-specific API client for `ReadMe Build
<https://readme.build>`_. It's based on the `api spec
<https://github.com/readmeio/api-spec>`_. 

Installation
============

.. code-block:: shell

  $ pip install api

Usage
=====

Here's how you call it:

.. code-block:: python

    import api
    api = api.config('...')

    val, res = api('temp-deprecated').run('sayHello', {
        'name': 'hi'
    })

    if res.error:
        print 'oh no'
    else:
        print val
    

Running tests
=============

*How do you run tests?*

Deploying to the package manager
================================

First, update the version in `setup.py`. Then run:

  python setup.py sdist upload -r pypi

Credits
=======

* Forked from https://github.com/p0bailey/python_pip
