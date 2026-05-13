# 🔗 AWS Serverless URL Shortener

A fully serverless URL shortener application built using AWS cloud services including Lambda, API Gateway, DynamoDB, S3, and CloudFront.

This project demonstrates modern cloud-native backend architecture using a scalable, event-driven, and cost-efficient serverless design.

---

# 🚀 Live Demo

### Frontend

https://d3461bhuac6sr6.cloudfront.net/

### API Endpoint

```text
https://d3ozu89ifj.execute-api.us-east-1.amazonaws.com/shorten
```

---

# 📸 Preview

## Frontend UI

![Frontend UI](images/Frontend%20UI.jpeg)

## AWS Architecture Diagram

![AWS Architecture Diagram](images/AWS%20Architecture%20Diagram.png)

---

# 🏗️ Architecture Overview

```text
User
  ↓
CloudFront CDN
  ↓
S3 Static Website Hosting
  ↓
API Gateway
  ↓
Lambda Functions
  ↓
DynamoDB
```

---

# 🔄 Request Flow

## URL Shortening Flow

```text
Frontend
   ↓
API Gateway (POST /shorten)
   ↓
Lambda: create_short_url
   ↓
DynamoDB
```

---

## Redirect Flow

```text
User opens short URL
   ↓
API Gateway (GET /{code})
   ↓
Lambda: redirect_url
   ↓
DynamoDB lookup
   ↓
HTTP 301 Redirect
```

---

# ✨ Features

* 🔗 Generate short URLs instantly
* ⚡ Fully serverless backend
* 📊 Click tracking support
* ☁️ Cloud-native AWS architecture
* 🌐 Static frontend hosting with S3
* 🚀 CloudFront CDN integration
* 🔒 IAM-based secure permissions
* 📈 CloudWatch logging & monitoring
* 💰 AWS Free Tier friendly

---

# 🛠️ Tech Stack

| Category       | Technology            |
| -------------- | --------------------- |
| Frontend       | HTML, CSS, JavaScript |
| Backend        | Python                |
| Cloud Provider | AWS                   |
| API Service    | API Gateway           |
| Compute        | AWS Lambda            |
| Database       | DynamoDB              |
| Hosting        | Amazon S3             |
| CDN            | CloudFront            |
| Monitoring     | CloudWatch            |
| Security       | IAM                   |

---

# 📂 Project Structure

```text
aws-url-shortener/
│
├── frontend/
│   └── index.html
│
├── lambda/
│   ├── create_short_url.py
│   └── redirect_url.py
│
├── screenshots/
│
├── architecture/
│   └── architecture-diagram.png
│
├── README.md
└── .gitignore
```

---

# ⚙️ AWS Services Used

## Amazon API Gateway

Used to expose REST API endpoints:

* `POST /shorten`
* `GET /{code}`

---

## AWS Lambda

### create_short_url

Responsible for:

* generating unique shortcodes
* storing URL mappings
* returning shortened URLs

### redirect_url

Responsible for:

* fetching original URLs
* incrementing click count
* redirecting users

---

## Amazon DynamoDB

Stores URL mappings in the format:

```json
{
  "shortcode": "abc123",
  "original_url": "https://google.com",
  "clicks": 5
}
```

---

## Amazon S3

Hosts the static frontend website.

---

## Amazon CloudFront

Provides:

* HTTPS support
* CDN caching
* low-latency delivery
* production-style deployment

---

## Amazon CloudWatch

Used for:

* Lambda execution logs
* debugging
* monitoring API activity

---

# 🔥 API Example

## Create Short URL

### Request

```bash
curl -X POST "https://YOUR_API_URL/shorten" \
-H "Content-Type: application/json" \
-d "{\"url\":\"https://google.com\"}"
```

---

### Response

```json
{
  "short_url": "https://your-domain.com/abc123",
  "code": "abc123"
}
```

---

# 🧠 Learning Outcomes

This project helped me understand:

* Serverless application architecture
* REST API development using AWS
* Lambda event-driven workflows
* NoSQL database design
* Static frontend deployment
* CDN integration with CloudFront
* IAM permission management
* Cloud monitoring and debugging
* Real-world cloud deployment workflows

---

# 🔐 Security Notes

* No AWS credentials or secrets are stored in the repository
* IAM roles are used for AWS service access
* Public frontend served via CloudFront CDN
* API exposed through API Gateway
* CloudWatch enabled for monitoring and debugging

---

# 📈 Future Improvements

Potential upgrades:

* Custom aliases
* QR code generation
* URL expiration support
* Analytics dashboard
* User authentication with Cognito
* Terraform IaC deployment
* CI/CD pipeline using GitHub Actions
* Custom domain using Route53

---

# 💰 Cost Optimization

This project is designed to remain within the AWS Free Tier for low traffic usage using:

* Lambda free requests
* DynamoDB free tier
* S3 static hosting
* CloudFront free usage limits

---

# 🚀 Deployment Services Used

* AWS Lambda
* API Gateway
* DynamoDB
* Amazon S3
* CloudFront
* CloudWatch
* IAM

---

# 👨‍💻 Author

Ganesh Kambli

Final Year Computer Engineering Student
Interested in Backend Development, Cloud Computing, Cybersecurity, and AWS Cloud Engineering

---

# ⭐ Project Goal

The goal of this project was to gain practical experience with real-world AWS serverless architecture and cloud deployment workflows while building a scalable and production-style application.
