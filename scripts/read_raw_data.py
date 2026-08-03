from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("API Data Pipeline") \
    .getOrCreate()

df = spark.read.json("data/raw/posts.json")

df.show(5)

df.printSchema()

print(f"Total Records: {df.count()}")

spark.stop()

