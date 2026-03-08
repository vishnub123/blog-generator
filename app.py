import boto3
import botocore.config
import json
from datetime import datetime

def blog_generator(topic: str) -> str:
    prompt = f"""<s>[INST] Generate a blog post in 300 words about {topic} 
    Assistent:[/INST]"""

    body={
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.6,
        "top_p": 0.9
    }

    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1",config=botocore.config.Config(read_time = 300, retries = {'max_attempts': 3}))
        response = bedrock.invoke_model(body=Json.dumps(body),model_id="protopia-llama-3-1-8b-instruct")
        response_content = response.get("body").read()
        response_data = json.loads(response_content)
        print(response_data)
        blog_details = response_data['generation']
        return blog_details
    except Exception as e:
        print(f"Error generating blog: {e}")
        return ""
def save_blog_to_s3(s3_key, s3_bucket):
    s3=boto3.client('s3')

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generated_blog)
        print(f"Blog saved to S3: {s3_key}")
    except Exception as e:
        print(f"Error saving blog to S3: {e}")
        return False
    return True


def lambda_handler(event, context):
    # TODO implement
    event = json.loads(event['body'])
    topic = event['topic']
    generated_blog = blog_generator(topic=topic)


    if generated_blog:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        s3_key = f"blog_posts/{current_time}_{topic}.txt"
        s3_bucket = "blog-generator-bucket"
        save_blog_to_s3(s3_key, s3_bucket)

    else:
        print("Error generating blog")

    return{
        'statusCode': 200,
        'body': json.dumps('Blog generated successfully')
    }
 