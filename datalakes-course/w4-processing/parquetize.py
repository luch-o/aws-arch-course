import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME", "SOURCE_DATABASE", "SOURCE_TABLE", "TARGET_PATH"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_source_node = glueContext.create_dynamic_frame.from_catalog(
    database=args["SOURCE_DATABASE"], table_name=args["SOURCE_TABLE"], transformation_ctx="S3bucket_source_node"
)

# Script generated for node S3 bucket
S3bucket_traget_node = glueContext.write_dynamic_frame.from_options(
    frame=S3bucket_source_node,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": args["TARGET_PATH"], "partitionKeys": []},
    transformation_ctx="S3bucket_traget_node",
)

job.commit()