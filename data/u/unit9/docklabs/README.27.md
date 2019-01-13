# Arachni security scanner

This image installs [`arachni`](http://www.arachni-scanner.com) security
scanner. Arachni is a feature-full, modular, high-performance Ruby framework
aimed towards helping penetration testers and administrators evaluate the
security of modern web applications.

Due to the difference in the way cli version of the scanner works over
the API, this image is using a very simple web UI to launch the console
scanner.

This image is using a simple [web ui](https://github.com/unit9/arachni-ui)
which is written in [`Flask`](http://flask.pocoo.org/),
[`Celery`](http://www.celeryproject.org/), and [`Redis`](https://redis.io/).
Celery is using a single worker so only one instance of the scanner can run
at the same time.

scanner source code has been patched to allow plain text reports.

Web UI is running on port 5000.

## Running the image

You need to pass the following environment variables:

- `DEBUG` - either 0 or 1, optional, set to 0
- `SCANNER_PATH` - absolute path to arachni scanner, e.g. `/bin/arachni`
- `SCANNER_REPORT_PATH` - path to a dir where to save reports
- `CC_EMAIL` - email address to send report to
- `BCC_EMAIL` - email address to send report to
- `FROM_EMAIL` - sender's email
- `SMTP_SERVER` - smtp server's address
- `SMTP_PORT` - smtp server's port, optional, set to 25
- `SMTP_USERNAME` - server's login, optional
- `SMTP_PASSWORD` - server's password, optional
- `CELERY_BROKER_URL` - [broker url](http://docs.celeryproject.org/en/latest/getting-started/brokers/index.html) for Celery
- `CELERY_RESULT_BACKEND` - [result backend](http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend) to store scan results

Here is an example of running the image:
```
docker run -it --rm --name arachni -p 8080:5000 -e CC_EMAIL=security@company.com -e BCC_EMAIL=it@company.com -e FROM_EMAIL=scanner@company.com -e SMTP_SERVER=smtp.company.com -e SMTP_PORT=587 -e DEBUG=1 -e CELERY_BROKER_URL="redis://redis:6379/0" -e CELERY_RESULT_BACKEND="redis://redis:6379/0" arachni:latest
```
