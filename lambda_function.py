import json
import csv
import os
import boto3
import pymysql

s3 = boto3.client('s3')
sns = boto3.client('sns')

host = os.environ['DB_HOST']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
database = os.environ['DB_NAME']
topic_arn = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):

    try:
        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']

            response = s3.get_object(Bucket=bucket, Key=key)
            csv_content = response['Body'].read().decode('utf-8').splitlines()

            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            cursor = connection.cursor()

            reader = csv.DictReader(csv_content)

            for row in reader:
                cursor.execute(
                    "INSERT INTO customers (id, name, email) VALUES (%s, %s, %s)",
                    (
                        row['id'],
                        row['name'],
                        row['email']
                    )
                )

            connection.commit()
            cursor.close()
            connection.close()

            sns.publish(
                TopicArn=topic_arn,
                Subject="Data Insertion Success",
                Message=f"File '{key}' was processed successfully and the customer records were inserted into the Amazon RDS database."
            )

        return {
            'statusCode': 200,
            'body': json.dumps('CSV imported successfully!')
        }

    except Exception as e:

        sns.publish(
            TopicArn=topic_arn,
            Subject="Data Insertion Failed",
            Message=str(e)
        )

        raise e