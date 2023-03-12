# Processing Data in a Data Lake

In this exercise, you define a database and configure a crawler to explore data in an Amazon S3 bucket. Next, you create a table. You then transform the comma-separated values (CSV) file into Parquet and create a table for the Parquet data. Finally, you query the data with Amazon Athena.

![Architecture Diagram](arch.png)

## Replication Instructions

Since this week's architecture doesn't have lambda functions and a CloudFormation stack is provided with an S3 Bucket to store the parquetized data, this exercise is done using CloudFormation only with the provided stack as a Nested Stack.

First, package the `main-stack.yml` so the template artifacts are uploaded to s3 and generate a  `main-stack-packaged.yml` ready to be deployed. You must provide an existing bucket in your account to upload the template's artifacts

```
aws cloudformation package \
--template-file main-stack.yml \
--s3-bucket YOUR_BUCKET \
--output-template-file main-stack-packaged.yml
```

Use the following command with the packaged template to deploy the stack:

```
aws cloudformation deploy \
--template-file main-stack-packaged.yml \
--stack-name nytaxi-processing \
--capabilities CAPABILITY_NAMED_IAM
```

To test everything is working as expected you can log into the Management Console and:
1. Run the csv crawler
2. Run the parquetize job
3. Run the parque crawler
4. Query your data in Athena

To detelete the stack, use the following command and remember to empty the S3 bucket before.

```
aws cloudformation delete-stack \
--stack-name nytaxi-processing
```

> **Note**: The script used to create the job was adapted from one generated automatilaccly using the visual editor, removing the ApplyMapping step and passing the source and target locations as arguments
