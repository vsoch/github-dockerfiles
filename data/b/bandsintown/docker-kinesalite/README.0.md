# About

This folder contains a sample application showing how to integrate Kinealite with a Lambda.

For now Kinesalite [does not support triggering Lambda](https://github.com/mhart/kinesalite/issues/39), 
but in the context of using Amazon Kinesis and AWS Lambda to process events we need to be able to reproduce 
this processing in local with Docker.

This application is composed of 4 components:

  - `app`: the application itself sending events through the `aws-sdk` client library to Kinesalite
  - `kinesis`: the Kinesalite server simulating Amazon Kinesis
  - `stream`: a convenient JS script just creating our `events` stream using the `aws-sdk` client library 
  - `lambda`: our lambda function wrapped in a container with a script managing the consumption of the stream
  
# How it works ?
  
When the application start (`docker-compose up` ) :
   
   - The `kinesalite`service starts first
   - The `stream` service create the `events` stream
   - The `app` starts and sends each 5 seconds new events to Kinesis (Kinesalite) (cron with [moment](https://github.com/moment/moment))
   - The `lambda` service consume each 5 seconds new events coming from Kinesis (cron with [moment](https://github.com/moment/moment)) and call the Lambda with [lambda-local](https://github.com/ashiina/lambda-local)
   
We tried to create a real trigger based on the change in the LevelDB log file using [Nodemon](https://github.com/remy/nodemon), but for some reasons
nodemon does not detect the changes in the DB, that's why we just setup a cron to consume events.
  