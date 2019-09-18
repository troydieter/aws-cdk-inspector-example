import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_inspector_poc",
    version="1.0.0",

    description="AWS Inspector CDK POC",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="odonoha@luxoft.com",
    package_dir={"": "cdk_inspector_poc"},
    packages=setuptools.find_packages(where="cdk_inspector_poc"),

    install_requires=[
        "aws-cdk.core",
        "attrs",
        "aws-cdk.assets",
        "aws-cdk.aws-apigateway",
        "aws-cdk.aws-applicationautoscaling",
        "aws-cdk.aws-autoscaling",
        "aws-cdk.aws-autoscaling-common",
        "aws-cdk.aws-autoscaling-hooktargets",
        "aws-cdk.aws-certificatemanager",
        "aws-cdk.aws-cloudformation",
        "aws-cdk.aws-cloudfront",
        "aws-cdk.aws-cloudwatch",
        "aws-cdk.aws-codebuild",
        "aws-cdk.aws-codecommit",
        "aws-cdk.aws-codepipeline",
        "aws-cdk.aws-ec2",
        "aws-cdk.aws-ecr",
        "aws-cdk.aws-ecr-assets",
        "aws-cdk.aws-ecs",
        "aws-cdk.aws-elasticloadbalancing",
        "aws-cdk.aws-elasticloadbalancingv2",
        "aws-cdk.aws-events",
        "aws-cdk.aws-events-targets",
        "aws-cdk.aws-iam",
        "aws-cdk.aws-inspector",
        "aws-cdk.aws-kms",
        "aws-cdk.aws-lambda",
        "aws-cdk.aws-logs",
        "aws-cdk.aws-route53",
        "aws-cdk.aws-route53-targets",
        "aws-cdk.aws-s3",
        "aws-cdk.aws-s3-assets",
        "aws-cdk.aws-secretsmanager",
        "aws-cdk.aws-servicediscovery",
        "aws-cdk.aws-sns",
        "aws-cdk.aws-sns-subscriptions",
        "aws-cdk.aws-sqs",
        "aws-cdk.aws-ssm",
        "aws-cdk.aws-stepfunctions",
        "aws-cdk.custom-resources",
        "aws-cdk.cx-api",
        "aws-cdk.region-info",
        "cattrs",
        "jsii",
        "publication",
        "python-dateutil",
        "six",
        "typing-extensions"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
