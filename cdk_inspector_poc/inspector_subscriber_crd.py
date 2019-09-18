from aws_cdk import (
    aws_cloudformation as cfn,
    aws_lambda as lambda_,
    aws_iam as iam,
    core
)
from uuid import uuid4


class InspectorSubscriberCustomResource(core.Construct):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        with open("crd_function/crd.py") as fp:
            code_body = fp.read()

        crd_lambda = lambda_.SingletonFunction(
            self, "Singleton",
            uuid=str(uuid4()),
            code=lambda_.InlineCode(code_body),
            handler="index.lambda_handler",
            timeout=core.Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_7,
        )
        crd_lambda.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=["inspector:SubscribeToEvent"],
                resources=["*"]
            )
        )

        resource = cfn.CustomResource(
            self, "Resource",
            provider=cfn.CustomResourceProvider.lambda_(handler=crd_lambda),
            properties=kwargs,
        )

        self.response = resource.get_att("Response").to_string()
