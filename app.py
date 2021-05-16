#!/usr/bin/env python3

from aws_cdk import core

from cdk_pipelines.pipeline_stack import PipelineStack

PIPELINE_ACCOUNT = '132260253285'

app = core.App()
PipelineStack(app, 'PipelineStack', env={
  'account': PIPELINE_ACCOUNT,
  'region': 'us-east-2',
})

app.synth()
