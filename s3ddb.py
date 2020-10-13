import boto3
s3_obj   = boto3.client("s3")
dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('empl')

def lambda_handler(event, context):

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object
    # S3 boto guide above

    bucket_name  = event['Records'][0]['s3']['bucket']['name']
    file_name    = event['Records'][0]['s3']['object']['key']

    resp = s3_obj.get_object(Bucket=bucket_name,Key=file_name)

    data = resp['Body'].read().decode('utf-8')
    employees = data.split('\n')

    for emp in employees:
        emp_id, emp_name, emp_prof = emp.split(',')

        # Adding data into Dynamo DB
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.put_item
        # DynamoDB Boto guide above.

        try:
            response = table.put_item(
                Item = {
                    "emp_id"   : emp_id,
                    "emp_name" : emp_name,
                    "emp_prof" : emp_prof
                }
            )
        except Exception, e:
            raise e
