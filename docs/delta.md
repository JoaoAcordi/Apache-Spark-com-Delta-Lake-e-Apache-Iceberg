# Delta Lake com Spark

## Modelo ER
![Modelo ER](imagens/modelo_er_delta.png)

## Estrutura da Tabela

```sql
CREATE TABLE IF NOT EXISTS top_filmes (
    titulo STRING,
    ano INT,
    nota DOUBLE
)
