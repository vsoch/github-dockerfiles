This content has moved to https://stackoverflow.com/c/theic/questions/176 and https://github.com/ixc/ixc-django-docker/commit/d26db0a19b61b9ded8c6606feebbf3cd288db932

# *Project Name*

*One or two lines describing the project: what is it, who is the client, URL of production site if there is one.*


## Technical Overview

*A more detailed technical summary, briefly listing key components used e.g. Django 1.8, GLAMkit/ICEkit with Collections*

*Consider adding a diagram if there are any non-trivial site integrations, unusual deployment arrangements, or anything that can be quickly expressed visually.*

Integrations:

*List any non-standard integrations here with a brief description, account name, who owns it, 1Password credentials, and a link to a more detailed Integrations document.*

* *PayPal Payments for ticket sales. Account name someaccount@client.com is owned by IC, see "PayPal - Some Client" in 1Password. Further details in `docs/integrations.md#paypal`*

Deployments:

*List deployed environments here with a brief description, URLs to the site itself and its hosting environment*

* ***Staging** for client acceptance and integration testing at https://staging.somesite.com*
  * *Site admin URL if non-obvious (e.g. `/kiosk/`)*
  * *Hosting URL, e.g. Docker Cloud stack name and URL*
  * *Any special instructions for accessing or maintaining site, e.g. access via VPN or via IC proxy server*

*Mention here if the deployments are monitored by external services like NewRelic, DataDog, PingDom etc with corresponding URLs.*


## Resources

Documentation:

* *Link to code repository location (the canonical location of this README document)*
* *Link to project technical documentation and diagrams, e.g. `docs/` directory in repo*
* *Link to ticketing system, e.g. GitHub or Assembla (if different from the main code repository, or if spread between different places)*
* *Link to project specs, client briefs etc e.g. a Google Team Drive directory*

Contacts:

* *Link to client's HubSpot URL, which will (ideally) be the single central repository of all the contact details below, otherwise*
* *If a HubSpot URL isn't available or appropriate, list details for:*
  * *IC staff member who acts as client contact or project manager*
  * *Client contact* 
  * *Any additional client- or project-specific communication channels, such as ZenDesk or Shared Slack Channels*
  * *Any relevant third-party service provider contacts, such as DNS provider or external design agency etc*


## Getting Started

*Link directly to a Getting Started guide document for new or returning developers, or include instructions here if they are **brief***

*For projects based on `ixc-django-docker` you can probably get away with something like the following...*

*This project is based on [ixc-django-docker](https://github.com/ixc/ixc-django-docker/). To get started:*

1. *Copy the `.env.local.sample` file to `.env.local` and fill in this file's `TRANSCRYPT_PASSWORD` value from 1Password*

2. *Create and start a Docker or Docker-like development shell, see https://github.com/ixc/ixc-django-docker/tree/11-improve-documentation#how-to-run-an-ixc-django-docker-project*

3. *Perform any project-specific steps, such as `manage.py createsuperuser` to create a super-user*

4. *Use the `ixc-django-docker` shell scripts to run the site, run tests, load data, etc, see (DOCS PENDING)*

5. *See [using-docker.md](./using-docker.md) for more details on using Docker for development.
