import boto3
# dynamodb = boto3.resource('dynamodb')
dynamodb = boto3.resource('dynamodb', aws_access_key_id=os.getenv("aws_access_key_id"),
                          aws_secret_access_key=os.getenv("aws_secret_access_key"), region_name='us-east-1')
table = dynamodb.Table(os.getenv("dynamodb.Table"))


def get_processed_items():
    response = table.get_item(Key={'id': 1})
    return response["Item"]


def set_processed_items(comments, submissions):
    response = table.put_item(
        Item={
            'id': 1,
            'c': comments,
            's': submissions
        },)
    print(response)
