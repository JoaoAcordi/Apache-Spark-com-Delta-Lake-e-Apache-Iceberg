# Apache Iceberg com Spark

## Modelo ER
![Modelo ER](docs/imagens/modeloERtop100_movies.png)

## Estrutura da Tabela

```sql
CREATE TABLE IF NOT EXISTS local.filmes.top100 (
    Rank STRING,
    Title STRING,
    Year STRING,
    Genre STRING,
    Director STRING,
    Main_Actor STRING,
    Country STRING,
    IMDb_Rating DOUBLE,
    Rotten_Tomatoes STRING,
    Runtime STRING,
    Language STRING,
    Oscars_Won STRING,
    Box_Office DOUBLE,
    Metacritic_Score STRING
);
