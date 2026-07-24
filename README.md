# AWS Serverless File Processing Pipeline

## Project Overview

This project demonstrates a serverless file processing pipeline built on Amazon Web Services (AWS). The solution automatically processes CSV files uploaded to Amazon S3, triggers an AWS Lambda function, stores customer records in Amazon RDS (MySQL), sends notifications using Amazon SNS, and monitors execution through Amazon CloudWatch.

---

## Architecture

Amazon S3
↓
AWS Lambda
↓
Amazon RDS (MySQL)
↓
Amazon SNS
↓
Amazon CloudWatch

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon RDS (MySQL)
- Amazon SNS
- ---

## Repository Structure

```text
aws-file-processing-pipeline/
├── README.md
├── LICENSE
├── Project-Documentation.pdf
├── architecture-diagram.png
├── lambda_function.py
├── employees.csv
└── screenshots/
    ├── s3-bucket.png
    ├── lambda.png
    ├── rds.png
    ├── sns.png
    ├── cloudwatch.png
    └── output.png
```

---

## Project Workflow

1. Upload a CSV file to Amazon S3.
2. Amazon S3 triggers an AWS Lambda function.
3. AWS Lambda reads and processes the CSV file.
4. Customer records are inserted into Amazon RDS (MySQL).
5. Amazon SNS sends a notification after successful processing.
6. Amazon CloudWatch monitors Lambda execution and logs.

---

## Key Features

- Automated CSV file processing
- Event-driven serverless architecture
- Secure IAM role-based access
- Data storage using Amazon RDS (MySQL)
- Email notifications using Amazon SNS
- Monitoring with Amazon CloudWatch
 
- ---

## Project Outcome

Successfully developed and deployed an event-driven serverless file processing pipeline on AWS. The solution automatically processes CSV files uploaded to Amazon S3, stores customer records in Amazon RDS, sends notifications using Amazon SNS, and monitors execution through Amazon CloudWatch.

---

## Author

**Isaac Anish Dass**

AWS Cloud & DevOps Engineer

GitHub: [isaac-cloud28](https://github.com/isaac-cloud28)

LinkedIn: [Isaac Anish Dass](https://linkedin.com/in/isaac-anish-cloud)
