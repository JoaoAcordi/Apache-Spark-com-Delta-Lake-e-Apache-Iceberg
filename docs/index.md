# Projeto: Apache Spark com Delta Lake e Apache Iceberg

Este projeto demonstra o uso das tecnologias **Apache Spark**, **Delta Lake** e **Apache Iceberg** para manipulação e versionamento de dados em um data lakehouse.

Os notebooks (`spark_delta.ipynb` e `spark_iceberg.ipynb`) realizam as operações de criação, inserção, atualização e exclusão em tabelas transacionais, utilizando dados públicos de filmes top 100.

## Estrutura do Repositório

- **spark_delta.ipynb** → notebook com operações Delta Lake  
- **spark_iceberg.ipynb** → notebook com operações Iceberg  
- **modelo ER/** → contém o diagrama da tabela  
- **warehouse_path/** → dados salvos via Iceberg  
- **spark-warehouse/** → dados salvos via Delta  

## Fonte de Dados

O dataset utilizado foi **Top 100 Filmes IMDb**, contendo colunas como título, diretor, país, nota IMDb e bilheteria.

📁 Arquivo: `top_100_movies_full_best_effort.csv`
