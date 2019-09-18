#!/usr/bin/env python3

from aws_cdk import core

from cdk_inspector_poc.cdk_inspector_poc_stack import CdkInspectorPocStack


app = core.App()
CdkInspectorPocStack(app, "aws-cdk-inspector-example", env={'region': 'eu-central-1'})

app.synth()
