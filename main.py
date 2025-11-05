from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("DeltaIcebergExample")
    .config("spark.jars.packages", "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", "warehouse_path")
    .getOrCreate()
)

print("Spark iniciado com sucesso com Iceberg!")