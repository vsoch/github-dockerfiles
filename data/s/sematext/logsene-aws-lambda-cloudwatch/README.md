![cloudwatch->Logsene](https://sematext.com/wp-content/uploads/2016/03/aws-cloudwatch.png)
# CloudWatch to Logsene AWS Lambda function
[AWS Lambda](https://aws.amazon.com/documentation/lambda/) function to send [CloudWatch](https://www.amazonaws.cn/en/cloudwatch/) logs to the [Logsene logging SaaS](https://sematext.com/logsene). As new log events are being stored in CloudWatch, this function would forward the events to your Logsene application.

## How To
This tutorial shows how to send CloudWatch logs to a Logsene application. The code in this repository can be used to send any CloudWatch logs to Logsene.  To illustrate how to do that we'll use [AWS VPC](https://aws.amazon.com/vpc/) logs,  for which this Lambda function happens to have built-in parsing. If you're using a type of CloudWatch logs that isn't supported yet, feel free to edit **pattern.yml** or to open an issue.

The main steps are:
 0. Create a Flow Log for your VPC, if there isn't one already. **If you're looking to ship other CloudWatch logs, just skip this step and go through the rest**.
 1. Create a new Lambda Function
 2. Clone this repository and fill in your Logsene Application Token, create a ZIP file with the contents of the cloned repository, and configure the new Lambda function to use the created ZIP file as code
 3. Decide on the maximum memory to allocate for this function and the timeout for its execution
 4. Explore your logs in Logsene :)

### Create a Flow Log
To start, log in to your AWS Console, then go to Services -> VPC. There, select your VPC, right-click it and select **Create Flow Log**:
![createflowlog](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/createflowlog.png)

Then you'll need to set up a IAM role that's able to push VPC logs to your CloudWatch account (if you don't have one already) and then choose a name for this flow. You'll use the name later on in the lambda function.
![flowlog](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/flowlog.png)

### Create a new AWS Lambda function
Now go to Services -> Lambda and get started with a new function. Then the first step is to select a blueprint for your function. Take **cloudwatch-logs-process-data**:
![blueprint](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/blueprint.png)

The next step is to select a source. Here you'd make sure the source type is CloudWatch Logs and select the flow you just created. You can filter only certain logs, but you'd normally leave the **Filter Pattern** empty to process all of them. Nevertheless, you need to give this filter a name:
![source](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/source.png)

At the next step, you'd configure the function itself. First you give it a name:
![name](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/name.png)

Then you have to specify the code.

### Add the code to your Lambda function
First you'd need to clone this repository:

    git@github.com:sematext/logsene-aws-lambda-cloudwatch.git

Optionally: Edit pattern.yml (see [logagent parser](http://sematext.github.io/logagent-js/parser/#how-does-the-parser-work)) for additional parser rules, depending on the structure of your logs. Note: The "sourceName"" in the pattern definition should match the AWS "logGroup". 

Now your code is ready, so you need to make a zip file out of it. **Note**: make sure you zip only the contents of the repository, not the directory containing the repository. The correct way to do it is something like this:

    pwd
    # /tmp/cloned-repos/logsene-aws-lambda-cloudwatch
    zip -r logsene.zip *

Finally, you'd upload the zip to AWS Lambda as the function code:
![upload](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/config_token_env_vars.png)

Set the Logsene application token in  **LOGSENE_TOKEN** environment variable. To find the Logsene Application Token, go to your [Sematext Account](https://apps.sematext.com), then in the Services menu select Logsene, and then the Logsene application you want to send your logs to. Once you're in that application, click the Integration button and you'll see the application token:
![token](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/token.png)


### Finalize the function configuration
After the code, leave the handler to the default *index.handler* and select a role that allows this function to execute. You can create a new Basic execution role to do that (from the drop-down) or select a basic execution role that you've already created:
![role](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/role.png)

Then, you need to decide on how much memory you allow for the function and how long you allow it to run. This depends on the log throughput (more logs will need more processing resources) and will influence costs (i.e. like keeping the equivalent general-purpose instance up for that time). Normally, runtime is very short so even large resources shouldn't generate significant costs. 256MB and 30 second timeout should be enough for most use-cases:
![memory](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/memory.png)

To enable the function to run when new logs come in, you'd need to enable the source with your Flow Log name at the last step.
![enable](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/enable.png)

### Exploring CloudTrail logs with Logsene
As logs get generated by VPC, the function should upload their contents to Logsene. You can use the native UI to explore those logs:
![native](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/native.png)

And because VPC logs get parsed out of the box, you can also use Kibana to generate visualizations. Like breaking down connections by the number of bytes:
![Kibana](https://raw.githubusercontent.com/sematext/logsene-aws-lambda-cloudwatch/master/img/kibana.png)

Happy Logsene-ing!

