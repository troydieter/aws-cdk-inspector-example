def lambda_handler(event, context):
    import logging as log
    log.getLogger().setLevel(log.INFO)

    # This needs to change if there are to be multiple resources
    # in the same stack
    physical_id = 'InspectorSNSSubscriber'

    try:
        import cfnresponse
        import boto3
        log.info('Input event: %s', event)

        # Check if this is a Create and we're failing Creates
        if event['RequestType'] == 'Create' and event['ResourceProperties'].get('FailCreate', False):
            raise RuntimeError('Create failure requested')
        template_arn = event['ResourceProperties']['Template']
        topic_arn = event['ResourceProperties']['Topic']
        inspector_client = boto3.client('inspector')
        log.info("Subscribing template %s to topic %s", template_arn, topic_arn)
        inspector_client.subscribe_to_event(
            resourceArn=template_arn,
            event="ASSESSMENT_RUN_COMPLETED",
            topicArn=topic_arn
        )
        cfnresponse.send(event, context, cfnresponse.SUCCESS,
                         {'Response': 'Template was subscribed to topic'}, physical_id)
    except Exception as e:
        log.exception(e)
        # cfnresponse's error message is always "see CloudWatch"
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, physical_id)