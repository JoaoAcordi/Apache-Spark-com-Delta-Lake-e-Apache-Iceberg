# 🚀 Apache Spark com Delta Lake e Apache Iceberg

Este projeto demonstra o uso do **Apache Spark** integrado com os formatos de armazenamento **Delta Lake** e **Apache Iceberg**.  
O objetivo é criar, manipular e versionar tabelas utilizando operações de **INSERT**, **UPDATE** e **DELETE**, com dados de filmes públicos.

---

## 🎬 Contexto do Projeto

O dataset utilizado é **"Top 100 Movies (Best Effort)"**, contendo informações sobre:
- Posição (`Rank`)
- Título (`Title`)
- Ano (`Year`)
- Diretor, Ator Principal, País, Idioma
- Avaliações de IMDb, Metacritic e Rotten Tomatoes
- Bilheteria (`Box_Office`)

O modelo ER (Entidade-Relacionamento) representa a entidade **Filme**, onde cada registro corresponde a um filme único.

---

## 🧩 Estrutura do Repositório

```
├── modelo ER/                      # Diagrama do modelo ER
├── spark_iceberg.ipynb             # Notebook com operações no Iceberg
├── spark_delta.ipynb               # Notebook com operações no Delta Lake
├── top_100_movies_full_best_effort.csv
├── warehouse_path/                 # Dados do Iceberg
├── spark-warehouse/                # Dados do Delta Lake
├── mkdocs.yml                      # Configuração do site MKDocs
├── docs/
│   ├── index.md                    # Página inicial
│   ├── iceberg.md                  # Página explicando Iceberg
│   └── delta.md                    # Página explicando Delta
└── README.md                       # Este arquivo
```

---

## ⚙️ Como Executar o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/JoaoAcordi/Apache-Spark-com-Delta-Lake-e-Apache-Iceberg.git
cd Apache-Spark-com-Delta-Lake-e-Apache-Iceberg
```

### 2. Crie e Ative um Ambiente Virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

> Caso o arquivo `requirements.txt` não exista, você pode instalar diretamente:
```bash
pip install pyspark delta-spark mkdocs
```

---

## 💾 Executando os Notebooks

Abra o **Jupyter Notebook** e rode:

```bash
jupyter notebook
```

- **spark_delta.ipynb** → manipulação com Delta Lake  
- **spark_iceberg.ipynb** → manipulação com Iceberg

Cada notebook mostra:
- Criação da tabela
- Inserção de registros
- Atualização (`UPDATE`)
- Exclusão (`DELETE`)
- Consulta (`SELECT`)

---

## 🌐 Gerando a Documentação com MKDocs

### 1. Inicie o servidor local
```bash
mkdocs serve
```

### 2. Acesse no navegador:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 3. Estrutura das páginas
- `/` → Visão geral do projeto  
- `/iceberg/` → Tabelas e exemplos de Iceberg  
- `/delta/` → Tabelas e exemplos de Delta Lake  

---

## 🧠 Modelo ER

O projeto utiliza uma única entidade principal:

**Filmes**
| Campo | Tipo | Descrição |
|--------|------|------------|
| Rank | STRING | Posição no ranking |
| Title | STRING | Nome do filme |
| Year | STRING | Ano de lançamento |
| Genre | STRING | Gênero |
| Director | STRING | Diretor |
| Main_Actor | STRING | Ator principal |
| Country | STRING | País de origem |
| IMDb_Rating | DOUBLE | Nota IMDb |
| Rotten_Tomatoes | STRING | Avaliação Rotten Tomatoes |
| Runtime | STRING | Duração |
| Language | STRING | Idioma |
| Oscars_Won | STRING | Prêmios do Oscar |
| Box_Office | DOUBLE | Bilheteria |
| Metacritic_Score | STRING | Nota Metacritic |

> 📷 O diagrama ER está na pasta `modelo ER/`.

---

## 📚 Créditos

- [Apache Spark](https://spark.apache.org/)
- [Delta Lake](https://delta.io/)
- [Apache Iceberg](https://iceberg.apache.org/)
- Dataset público: *Top 100 Movies (Best Effort)*

---

## ✨ Autor

**João Acordi**  
Projeto desenvolvido para demonstração de manipulação de tabelas em formatos Lakehouse (Delta & Iceberg) utilizando Apache Spark.

---
