# Pingeon - notification microservice

## About

This project uses [Feathers](http://feathersjs.com). An open source web  framework for building modern real-time applications.

## Getting Started

1. Make sure you have [NodeJS](https://nodejs.org/) and [npm](https://www.npmjs.com/) installed.
2. Install your dependencies
    
    ```
    cd path/to/pingeon; npm install
    ```

3. Start your app
    
    ```
    npm start
    ```

## Environment Variables

```
DEBUG - All in app logs goes to 'app*'.
PORT - What port server is listening.

AMQP_URL - RabbitMQ url.
DATABASE_URL - db connection url.

PUBSUB_ID - pub/sub provider id.
PUBSUB_KEY - pub/sub provider secret key.

EMAIL_KEY - email provider secret key. 
EMAIL_FROM - for example noreply@tep.io
EMAIL_DEFAULT_VARS - defaults vars used in email templates
EMAIL_TEMPLATE_MAPS - map template name and template id.

PUSH_KEY - AWS key.
PUSH_SECRET - AWS secret.
PUSH_REGION - AWS SNS region.
PUSH_TITLE - Title for push notifications.
APPS_ARNS - Object with arn for every app. Example: {
  "android": "arn:aws:sns:us-east-1:093525834944:app/GCM/android",
  "ios": "arn:aws:sns:us-east-1:093525834944:app/APNS/ios"
}
DEFAULT_APP - default app from the list above.

SENTRY_DSN - DSN from getsentry.com
```

## Email

Pingeon pass own template variables to help you automate email sending:
- firstName - recipient's first name;
- toEmail - recipient's email;
- currentYear - guess what.

As template Pingeon can use template id or your own name. Just set in env var `EMAIL_TEMPLATE_MAPS`:
```json
{
  "templateName" : "templateId"
}
```

## API

API Docs - [http://docs.pingeon.apiary.io](http://docs.pingeon.apiary.io)

## Testing

Simply run `npm test` and all your tests in the `test/` directory will be run.

## License

Copyright (c) 2016

Licensed under the [MIT license](LICENSE).
