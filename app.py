#!/usr/bin/env python3

from constructs import Construct
from aws_cdk import App, Stack

from cdk_inspector_poc.cdk_inspector_poc_stack import CdkInspectorPocStack


app = App()
CdkInspectorPocStack(app, "aws-cdk-inspector-example", env={'region': 'eu-central-1'})

app.synth()
