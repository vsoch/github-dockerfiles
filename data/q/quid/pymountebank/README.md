Mountebank
==========

This is a simple wrapper library around mountebank. It's useful for
mocking HTTP API services.

Usage
-----

::

    from mountebank import Imposter

    imposter = Imposter()
    imposter.add_stub("/test", "GET", "What I'm expecting")
    with imposter.mockhttp() as url:
        assert requests.get(url + "/test").text == "What I'm expecting"

Development
-----------

To run the containers:

::

    docker-compose up --build

To test:

::

    docker-compose exec tests /bin/bash -c "cd /apps/mountebank/tests;pytest"
    docker-compose exec tests2 /bin/bash -c "cd /apps/mountebank/tests;pytest"
