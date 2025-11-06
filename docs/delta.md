# Delta Lake com Spark

## Modelo ER
![Modelo ER](docs/imagens/modeloERtop100_movies.png)

## Estrutura da Tabela

```sql
CREATE TABLE IF NOT EXISTS top_filmes (
    titulo STRING,
    ano INT,
    nota DOUBLE
)
