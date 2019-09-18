
# Simple AWS Inspector CDK Proof-of-concept

## Prerequisites

Based on AWS CDK 1.4.0

To get started with CDK, follow [Amazon's own manual](https://aws.amazon.com/blogs/developer/getting-started-with-the-aws-cloud-development-kit-and-python/).

## Description

This code will deploy simple and rudimentary AWS Inspector setup in single region, consisting of:

* Inspector resource group, which will group EC2 instances with tag "Inspector: true"
* Inspector target, pointing at this resource group
* Inspector assessment template, containing rule packages, according to which instances will be assessed
* SNS topic, which will receive notification when assessment is completed
* Lambda function, that will be triggered by SNS topic and process report (it does nothing in this POC)
* Custom resource definition, which will subscribe inspector template to SNS topic (this doesn't happen automatically otherwise)

This setup is fully functional and can be modified for day-to-day use.

## Generating CloudFormation template

After installing and configuring CDK you can synthesize the CloudFormation template for this code.

```bash
cdk synth
```

## Adding new dependencies

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

# Useful commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy --profile profile_name`      deploy this stack to AWS account/region using AWS credentials profile called `profile_name`
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation

Enjoy!
