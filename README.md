# AI Blog Generator (AWS Lambda + Amazon Bedrock + S3)

## 📌 Project Overview
This project is a **serverless AI blog generator** that automatically generates a **300-word blog post from a given topic** using a Large Language Model hosted on Amazon Bedrock and stores the generated blog in Amazon S3.

The system exposes an API endpoint that can be tested using Postman.

When a user sends a topic, the system:
1. Sends the prompt to an LLM through Amazon Bedrock
2. Generates a blog post
3. Stores the generated blog in an S3 bucket
4. Returns a success response

This architecture uses a **serverless approach**, meaning no server management is required.

---

# 🏗 Architecture

```
User Request
     ↓
API Gateway
     ↓
AWS Lambda
     ↓
Amazon Bedrock (LLM)
     ↓
Generate Blog
     ↓
Store Blog in S3
     ↓
Return API Response
```

---

# 🚀 Technologies Used

- Python  
- AWS Lambda  
- Amazon Bedrock  
- Amazon S3  
- Postman  
- Boto3 (AWS SDK for Python)

---

# ⚙️ Project Components

## 1️⃣ AWS Lambda
AWS Lambda is a **serverless compute service** that runs backend code without managing servers.

In this project Lambda:
- Receives the topic from an API request
- Calls the Bedrock model to generate a blog
- Saves the generated blog to S3

### Lambda Entry Function

```python
def lambda_handler(event, context):
    event = json.loads(event['body'])
    topic = event['topic']
    generated_blog = blog_generator(topic=topic)
```

Lambda automatically scales and runs only when triggered.

---

## 2️⃣ Amazon Bedrock
Amazon Bedrock provides access to **foundation models (LLMs)** via API.

In this project Bedrock:
- Receives a prompt with the blog topic
- Generates a 300-word blog post

### Prompt Example

```python
prompt = f"""<s>[INST] Generate a blog post in 300 words about {topic} [/INST]"""
```

Model used:

```
protopia-llama-3-1-8b-instruct
```

---

## 3️⃣ Amazon S3
Amazon S3 is a **cloud storage service** used to store generated blog posts.

Each generated blog is stored with a timestamp.

Example stored file:

```
blog_posts/2026-03-09_Artificial_Intelligence.txt
```

Example code:

```python
s3.put_object(
    Bucket=s3_bucket,
    Key=s3_key,
    Body=generated_blog
)
```

Benefits:
- Scalable storage
- High durability
- Easy file retrieval

---

## 4️⃣ Postman
Postman is an API testing tool used to send HTTP requests to backend services.

It helps test the Lambda API endpoint.

### Example Request

**Method**

```
POST
```

**Endpoint**

```
https://api-id.execute-api.region.amazonaws.com/blog
```

**Body**

```json
{
  "topic": "Artificial Intelligence in Healthcare"
}
```

### Example Response

```json
{
  "message": "Blog generated successfully"
}
```

After sending the request, the blog is generated and stored in S3.

---

# 📂 Project Structure

```
blog-generator
│
├── lambda_function.py
├── README.md
└── requirements.txt
```

---

# 🔄 Workflow

1️⃣ User sends topic using Postman  
2️⃣ API Gateway triggers Lambda function  
3️⃣ Lambda sends prompt to Amazon Bedrock  
4️⃣ Bedrock generates blog content  
5️⃣ Lambda stores blog in S3  
6️⃣ API returns success response  

---

# ✨ Features

- Serverless architecture
- AI-powered blog generation
- Automatic cloud storage
- API testing with Postman
- Scalable and cost-efficient
