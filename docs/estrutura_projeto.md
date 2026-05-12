# 📁 Estrutura do Projeto — Sol para Todos

Este documento descreve a organização das pastas e arquivos do projeto **Sol para Todos**.

---

# 🏗 Estrutura Geral

```text
/sol-para-todos
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env
│
├── /database
│   ├── schema.sql
│   ├── inserts.sql
│   ├── queries.sql
│   └── backups/
│
├── /backend
│   ├── app.py
│   ├── database.py
│   │
│   ├── /routes
│   │   ├── usuario_routes.py
│   │   ├── simulacao_routes.py
│   │   ├── parceiro_routes.py
│   │   └── lead_routes.py
│   │
│   ├── /services
│   │   ├── usuario_service.py
│   │   ├── simulacao_service.py
│   │   └── lead_service.py
│   │
│   └── /sql
│       ├── usuario_sql.py
│       ├── simulacao_sql.py
│       └── lead_sql.py
│
├── /frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── /postman
│   ├── sol_para_todos_collection.json
│   └── README.md
│
└── /docs
    ├── DER.png
    ├── modelo_logico.pdf
    ├── requisitos_funcionais.docx
    └── apresentacao.pdf
```

---

# 📂 Pasta `/database`

Responsável pelos arquivos relacionados ao banco de dados PostgreSQL.

## Arquivos

### `schema.sql`
Contém os scripts de criação das tabelas, constraints, chaves primárias e chaves estrangeiras.

Exemplos:
- CREATE TABLE
- PRIMARY KEY
- FOREIGN KEY
- CHECK
- UNIQUE

---

### `inserts.sql`
Contém dados iniciais para testes e população do banco.

Exemplos:
- usuários fictícios;
- parceiros de teste;
- soluções padrão.

---

### `queries.sql`
Arquivo utilizado para armazenar consultas SQL úteis durante o desenvolvimento.

Exemplos:
- SELECT;
- JOIN;
- consultas analíticas;
- consultas de validação.

---

### `/backups`
Pasta destinada a backups do banco de dados.

---

# 📂 Pasta `/backend`

Responsável pela lógica da aplicação em Python.

---

## Arquivos principais

### `app.py`
Arquivo principal da aplicação Flask.

Responsável por:
- iniciar o servidor;
- configurar a aplicação;
- registrar rotas.

---

### `database.py`
Responsável pela conexão com o PostgreSQL.

Exemplos:
- psycopg2.connect();
- gerenciamento de conexão.

---

# 📂 Pasta `/routes`

Define os endpoints e rotas da aplicação.

## Arquivos

### `usuario_routes.py`
Rotas relacionadas ao usuário.

---

### `simulacao_routes.py`
Rotas relacionadas às simulações.

---

### `parceiro_routes.py`
Rotas relacionadas aos parceiros.

---

### `lead_routes.py`
Rotas relacionadas aos leads.

---

## Responsabilidades das rotas

- receber requisições HTTP;
- chamar regras de negócio;
- retornar respostas da API.

---

# 📂 Pasta `/services`

Responsável pelas regras de negócio do sistema.

## Arquivos

### `usuario_service.py`
Regras relacionadas aos usuários.

---

### `simulacao_service.py`
Regras relacionadas às simulações.

---

### `lead_service.py`
Regras relacionadas aos leads.

---

## Exemplos de regras de negócio

- cálculo de economia estimada;
- validação de dados;
- recomendação de soluções;
- atualização de status de leads.

---

# 📂 Pasta `/sql`

Armazena queries SQL organizadas por entidade.

## Arquivos

### `usuario_sql.py`
Queries SQL da entidade usuário.

---

### `simulacao_sql.py`
Queries SQL da entidade simulação.

---

### `lead_sql.py`
Queries SQL da entidade lead.

---

## Objetivo

- separar SQL do restante do código;
- facilitar manutenção;
- melhorar organização do backend.

---

# 📂 Pasta `/frontend`

Responsável pela interface da aplicação.

## Arquivos

### `index.html`
Estrutura da interface.

---

### `style.css`
Estilização da aplicação.

---

### `script.js`
Interações da interface e comunicação com backend.

---

# 📂 Pasta `/postman`

Responsável pelos testes da API da aplicação.

## Arquivos

### `sol_para_todos_collection.json`

Collection do Postman contendo:
- endpoints;
- testes CRUD;
- requisições organizadas por entidade.

Exemplos:
- Usuário;
- Simulação;
- Parceiro;
- Lead.

---

### `README.md`

Documentação dos testes da API.

Pode conter:
- instruções de importação;
- exemplos de JSON;
- descrição dos endpoints;
- exemplos de respostas da API.

---

## Objetivo

A pasta `/postman` permite:
- validar o funcionamento da API;
- testar endpoints sem frontend;
- facilitar integração entre backend e frontend;
- padronizar testes entre os integrantes do grupo.

---

# 📂 Pasta `/docs`

Armazena toda documentação do projeto.

## Arquivos

### `DER.png`
Diagrama Entidade Relacionamento.

---

### `modelo_logico.pdf`
Modelo lógico do banco de dados.

---

### `requisitos_funcionais.docx`
Documento de requisitos funcionais.

---

### `apresentacao.pdf`
Slides e materiais da apresentação.

---

# 📄 Arquivos da raiz

---

## `README.md`

Arquivo principal do repositório.

Contém:
- descrição do projeto;
- tecnologias utilizadas;
- instruções de execução;
- contexto acadêmico.

---

## `requirements.txt`

Lista de dependências Python utilizadas no projeto.

Exemplo:

```text
flask
psycopg2-binary
python-dotenv
bcrypt
```

---

## `.gitignore`

Define arquivos e pastas que não devem ser enviados ao GitHub.

Exemplos:
- venv/;
- __pycache__/;
- .env.

---

## `.env`

Arquivo de variáveis sensíveis da aplicação.

Exemplo:

```env
DB_HOST=localhost
DB_NAME=sol_para_todos
DB_USER=postgres
DB_PASSWORD=123456
```

⚠️ Este arquivo não deve ser enviado para repositórios públicos.

---

# ✅ Objetivo da Estrutura

A estrutura foi definida para:
- facilitar manutenção;
- melhorar organização;
- separar responsabilidades;
- permitir trabalho colaborativo;
- aproximar o projeto de uma estrutura real de mercado.
