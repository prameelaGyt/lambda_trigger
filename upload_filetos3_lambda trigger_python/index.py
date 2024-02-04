import boto3

s3_client = boto3.client('s3')

async def stream_to_string(stream):
    chunks = []
    async for chunk in stream.iter_chunks():
        chunks.append(chunk)
    return b''.join(chunks).decode('utf-8')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    data = await stream_to_string(response['Body'])
    print(data)
