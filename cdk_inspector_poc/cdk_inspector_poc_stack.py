from aws_cdk import aws_inspector as inspector
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as sns_subs
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda
from aws_cdk import core
from inspector_subscriber_crd import InspectorSubscriberCustomResource


class CdkInspectorPocStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        sns_principals_mapping = core.CfnMapping(
            scope=self,
            id="Inspector SNS Principals",
            mapping={
                "eu-central-1": {
                    "ARN": "arn:aws:iam::537503971621:root"
                },
                "us-east-1": {
                    "ARN": "arn:aws:iam::316112463485:root"
                },
                "eu-west-1": {
                    "ARN": "arn:aws:iam::357557129151:root"
                },
                "us-east-2": {
                    "ARN": "arn:aws:iam::646659390643:root"
                },
            }
        )

        inspector_rules_mapping = core.CfnMapping(
            scope=self,
            id="Inspector Rule packages",
            mapping={
                "eu-central-1": {
                    "CVE": "arn:aws:inspector:eu-central-1:537503971621:rulespackage/0-wNqHa8M9",
                    "CIS": "arn:aws:inspector:eu-central-1:537503971621:rulespackage/0-nZrAVuv8",
                    "securityBestPractices": "arn:aws:inspector:eu-central-1:537503971621:rulespackage/0-ZujVHEPB",
                    "runtimeBehaviorAnalysis": "arn:aws:inspector:eu-central-1:537503971621:rulespackage/0-0GMUM6fg"
                },
                "eu-west-1": {
                    "CVE": "arn:aws:inspector:eu-west-1:357557129151:rulespackage/0-ubA5XvBh",
                    "CIS": "arn:aws:inspector:eu-west-1:357557129151:rulespackage/0-sJBhCr0F",
                    "securityBestPractices": "arn:aws:inspector:eu-west-1:357557129151:rulespackage/0-SnojL3Z6",
                    "runtimeBehaviorAnalysis": "arn:aws:inspector:eu-west-1:357557129151:rulespackage/0-lLmwe1zd"
                },
                "us-east-1": {
                    "CVE": "arn:aws:inspector:us-east-1:316112463485:rulespackage/0-gEjTy7T7",
                    "CIS": "arn:aws:inspector:us-east-1:316112463485:rulespackage/0-rExsr2X8",
                    "securityBestPractices": "arn:aws:inspector:us-east-1:316112463485:rulespackage/0-R01qwB5Q",
                    "runtimeBehaviorAnalysis": "arn:aws:inspector:us-east-1:316112463485:rulespackage/0-gBONHN9h"
                },
                "us-east-2": {
                    "CVE": "arn:aws:inspector:us-east-2:646659390643:rulespackage/0-JnA8Zp85",
                    "CIS": "arn:aws:inspector:us-east-2:646659390643:rulespackage/0-m8r61nnh",
                    "securityBestPractices": "arn:aws:inspector:us-east-2:646659390643:rulespackage/0-AxKmMHPX",
                    "runtimeBehaviorAnalysis": "arn:aws:inspector:us-east-2:646659390643:rulespackage/0-UCYZFKPV"
                },
            }
        )

        resource_group = inspector.CfnResourceGroup(
            scope=self,
            id="CDK test resource group",
            resource_group_tags=[core.CfnTag(key="Inspector", value="true")]
        )
        assessment_target = inspector.CfnAssessmentTarget(
            scope=self,
            id="CDK test assessment target",
            resource_group_arn=resource_group.attr_arn
        )
        assessment_template = inspector.CfnAssessmentTemplate(
            scope=self,
            id="CDK test assessment template",
            assessment_target_arn=assessment_target.attr_arn,
            duration_in_seconds=300,
            rules_package_arns=[
                inspector_rules_mapping.find_in_map(self.region, package) for package in (
                    "CVE", "CIS", "securityBestPractices", "runtimeBehaviorAnalysis"
                )
            ]
        )
        report_function = aws_lambda.Function(
            scope=self,
            id="CDK Inspector test report processor",
            code=aws_lambda.Code.from_asset("report_function"),
            handler="report.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_7
        )
        topic = sns.Topic(
            scope=self,
            id="CDK Inspector topic"
        )

        topic.add_to_resource_policy(
            statement=iam.PolicyStatement(
                actions=["SNS:Publish"],
                principals=[iam.ArnPrincipal(arn=sns_principals_mapping.find_in_map(self.region, "ARN"))],
                resources=[topic.topic_arn]
            )
        )
        topic.add_subscription(
            subscription=sns_subs.LambdaSubscription(fn=report_function)
        )

        subscriber = InspectorSubscriberCustomResource(
            scope=self,
            id="Inspector SNS Subscriber",
            Template=assessment_template.attr_arn,
            Topic=topic.topic_arn
        )
