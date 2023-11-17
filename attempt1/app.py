import boto3
from h2o_wave import main, app, Q, ui

def list_aws_resources_for_user(user):
    aws_session = boto3.Session(profile_name = user)

    
    # Example: List EC2 Instances
    ec2_client = aws_session.client('ec2')
    ec2_instances = ec2_client.describe_instances()
    ec2_output = "\nEC2 Instances:"
    for reservation in ec2_instances.get('Reservations', []):
        for instance in reservation.get('Instances', []):
            ec2_output += f"\n  ID: {instance['InstanceId']}, Type: {instance['InstanceType']}"

    # Example: List S3 buckets
    s3_client = aws_session.client('s3')
    s3_buckets = s3_client.list_buckets()
    s3_output = "\nS3 Buckets:"
    for bucket in s3_buckets.get('Buckets', []):
        s3_output += f"\n  Name: {bucket['Name']}"

    # Example: List RDS instances
    rds_client = aws_session.client('rds')
    rds_instances = rds_client.describe_db_instances()
    rds_output = "\nRDS Instances:"
    for rds_instance in rds_instances.get('DBInstances', []):
        rds_output += f"\n  ID: {rds_instance['DBInstanceIdentifier']}"

    # Only include sections with content
    outputs = [output for output in [ec2_output, s3_output, rds_output] if output.split(":")[1].strip()]
    return "\n".join(outputs)

@app('/listing')
async def serve(q: Q):
    q.page['card1'] = ui.form_card(box='1 1 2 2', items=[
        ui.text(content='List of Users'),
        ui.button(name='User1', label='User 1'),
        ui.button(name='User2', label='User 2'),
        ui.button(name='User3', label='User 3'),
    ])

    if q.args.User1:
        aws_output = list_aws_resources_for_user('user1')
        q.page['card2'] = ui.form_card(box='4 1 2 2', items=[
            ui.text(content=f'AWS Resources for User 1:{aws_output}'),
        ])

    elif q.args.User2:
        aws_output = list_aws_resources_for_user('user2')
        q.page['card2'] = ui.form_card(box='4 1 2 2', items=[
            ui.text(content=f'AWS Resources for User 2:{aws_output}'),
        ])

    # elif q.args.User3:
    #     aws_output = list_aws_resources_for_user('user3')
    #     q.page['card2'] = ui.form_card(box='6 1 2 2', items=[
    #         ui.text(content=f'AWS Resources for User 3:{aws_output}'),
    #     ])

    await q.page.save()
