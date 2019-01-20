# ECS Example Architecture: Continuous Deployment

The EntropyZero Consulting, LLC Continuous Deployment example architecture demonstrates continuous deployment of a ruby application to Amazon ECS using AWS CodePipeline, AWS CodeBuild, and AWS CloudFormation. With continuous deployment, software revisions are deployed to a production environment automatically without explicit approval from a developer, making the entire software release process automated.

Launching this AWS CloudFormation stack provisions a continuous deployment process that uses AWS CodePipeline to monitor a GitHub repository for new commits, AWS CodeBuild to create a new Docker container image and to push it into Amazon ECR, and AWS CloudFormation to deploy the new container image to production on Amazon ECS.

## Running the example

#### 1. Fork the GitHub repository

Fork the [EntropyZero CI CD Example](https://github.com/EntropyZero/entropyzero-ci-cd-example) GitHub repository into your GitHub account.

From your terminal application, execute the following command (make sure to replace `<your_github_username>` with your actual GitHub username):

```console
git clone https://github.com/<your_github_username>/entropyzero-ci-cd-example
```

This creates a directory named `entropyzero-ci-cd-example` in your current directory, which contains the code for the example app.

#### 2. Create the CloudFormation stack

Choose **Deploy to AWS** to launch the template in your account.

**N. Virginia** (us-east-1) [![Launch Stack into N. Virginia with CloudFormation](/images/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=entropyzero-ci-cd-example&templateURL=https://s3.amazonaws.com/e0-example-continuous-deployment/e0-example-continuous-deployment.yaml)

The CloudFormation template requires the following parameters:

- GitHub configuration
  - **Repo**: The repo name of the sample service.  This should be the local fork of the EntropyZero CI CD Example repository.
  - **Branch**: The branch of the repo to deploy continuously.
  - **User**: Your username on GitHub.
  - **Personal Access Token**: Token for the user specified above. ([https://github.com/settings/tokens](https://github.com/settings/tokens))

The CloudFormation stack provides the following output:

- **ServiceUrl**: The sample service that is being continuously deployed.
- **PipelineUrl**: The continuous deployment pipeline in the AWS Management Console.

### Testing the example

After the CloudFormation stack is created, the latest commit to the GitHub repository is run through the pipeline and deployed to ECS. Open the **PipelineUrl** to watch the first revision run through the CodePipeline pipeline. After the deploy step turns green, open the URL from **ServiceUrl** which loads the example application.

To test continuous deployment, make a change to ExampleApplication/app/views/welcome/home.html.erb in the repository and push it to GitHub. CodePipeline detects the change, builds the new application, and deploys it to your cluster automatically. After the pipeline finishes deploying the revision, reload the page to see the changes made.

### Cleaning up the example resources

To remove all resources created by this example, do the following:

1. Delete the main CloudFormation stack which deletes the substacks and resources.

## License

This example is [licensed][license] under Apache 2.0 and is based on the ECS reference architecture from aws-labs,
https://github.com/awslabs/ecs-refarch-continuous-deployment

[license]: AWS_CI_CD_Configuration/LICENSE
