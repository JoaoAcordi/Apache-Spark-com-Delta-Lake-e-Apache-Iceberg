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

print("Extensões ativas:", spark.conf.get("spark.sql.extensions"))
print("Catálogos disponíveis:", spark.catalog.listDatabases())

print("Spark iniciado com Iceberg!")

spark.sql("CREATE DATABASE IF NOT EXISTS local.filmes")
spark.sql("""
    CREATE TABLE IF NOT EXISTS local.filmes.top100 (
        titulo STRING,
        ano INT,
        nota DOUBLE
    )
    USING iceberg
""")

spark.sql("SHOW DATABASES").show()

print("Tabela Iceberg criada com sucesso!")

spark.sql("CREATE DATABASE IF NOT EXISTS filmes_db;")
spark.sql("USE filmes_db;")

csv_path = "top_100_movies_full_best_effort.csv"
df = spark.read.option("header", True).csv(csv_path)
print("Dataset carregado!")
df.show(5)

df.writeTo("local.filmes_db.top_filmes").createOrReplace()
print("Tabela Iceberg criada!")

print("Exemplo SELECT:")
spark.sql("SELECT * FROM local.filmes_db.top_filmes LIMIT 5").show()

# Exemplo INSERT (ajustaremos os campos reais depois)
# spark.sql("""
# INSERT INTO local.filmes_db.top_filmes VALUES ('New Movie', 2025, 'New Director', 9.5)
# """)

# Exemplo UPDATE
# spark.sql("""
# UPDATE local.filmes_db.top_filmes
# SET rating = 9.9
# WHERE title = 'The Shawshank Redemption'
# """)

# Exemplo DELETE
# spark.sql("""
# DELETE FROM local.filmes_db.top_filmes
# WHERE year < 2000
# """)

print("Operações finalizadas!")

spark.stop()
