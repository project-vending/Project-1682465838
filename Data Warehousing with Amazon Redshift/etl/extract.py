python
import boto3
import csv
import os

S3_BUCKET_NAME = "your-bucket-name"
S3_INPUT_PATH = "input/data_source_1.csv"
OUTPUT_PATH = "output/extracted_data.csv"

# Connect to S3
s3 = boto3.resource("s3")

# Retrieve file from S3 bucket
bucket = s3.Bucket(S3_BUCKET_NAME)
obj = bucket.Object(S3_INPUT_PATH)
body = obj.get()["Body"].read().decode("utf-8")

# Write data to output file
with open(OUTPUT_PATH, "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_reader = csv.reader(body.splitlines())

    for row in csv_reader:
        csv_writer.writerow(row)
