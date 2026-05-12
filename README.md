# ☀️ Sol para Todos

Projeto acadêmico desenvolvido na disciplina de Banco de Dados com foco na democratização do acesso à energia solar para populações de baixa renda e comunidades com difícil acesso à infraestrutura elétrica.

---

# 🎯 Objetivo

O projeto busca conectar usuários a soluções acessíveis de energia solar, como:
- financiamentos;
- cooperativas;
- programas sociais;
- empresas parceiras.

A plataforma permite:
- cadastro de usuários;
- cadastro de parceiros;
- simulações de economia energética;
- recomendação de soluções;
- geração de leads entre usuários e parceiros.

---

# 🧠 Problema

Apesar do crescimento da energia solar no Brasil, grande parte da população ainda enfrenta dificuldades para acessar essa tecnologia devido a:
- alto custo inicial;
- falta de informação;
- dificuldade de acesso em regiões isoladas;
- desigualdade social e energética.

---

# 🚀 Tecnologias Utilizadas

## Backend
- Python
- Flask

## Banco de Dados
- PostgreSQL
- SQL puro

## Frontend
- HTML
- CSS
- JavaScript

## Testes de API
- Postman

## Versionamento
- Git
- GitHub

---

# 🏗 Estrutura do Projeto

```text
/sol-para-todos
│
├── /database
├── /backend
├── /frontend
├── /postman
└── /docs
```

Documentação completa da estrutura:
👉 `docs/estrutura_projeto.md`

---

# 📊 Funcionalidades

- Cadastro de usuários;
- Cadastro de parceiros;
- Simulação de economia solar;
- Recomendação de soluções;
- Gestão de leads;
- Histórico de simulações.

---

# 🗂 Modelagem de Banco

O projeto possui:
- DER (Diagrama Entidade Relacionamento);
- Modelo lógico;
- Cardinalidades;
- CRUD mapeado;
- Requisitos funcionais.

Os documentos estão disponíveis na pasta `/docs`.

---

# 🧪 Testes da API

Os testes da API são realizados utilizando o Postman.

A collection utilizada no projeto está disponível em:

```text
/postman
```

Os testes incluem:
- CRUD de usuários;
- CRUD de simulações;
- CRUD de parceiros;
- CRUD de leads;
- validações de integração com PostgreSQL.

---

# 🔌 Fluxo da Aplicação

```text
Postman / Frontend
↓
Backend Flask (Python)
↓
PostgreSQL
```

---

# ⚙️ Como Executar

## 1. Clonar o repositório

```bash
git clone https://github.com/seu-repo/sol-para-todos.git
```

---

## 2. Entrar na pasta do projeto

```bash
cd sol-para-todos
```

---

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Criar banco PostgreSQL

Criar um banco chamado:

```text
sol_para_todos
```

---

## 5. Configurar o `.env`

```env
DB_HOST=localhost
DB_NAME=sol_para_todos
DB_USER=postgres
DB_PASSWORD=sua_senha
```

---

## 6. Executar os scripts SQL

Utilizar os arquivos da pasta:

```text
/database
```

Executar:
- `schema.sql`
- `inserts.sql`

---

## 7. Executar a aplicação

```bash
python app.py
```

---

# 👥 Equipe

Projeto desenvolvido por alunos da disciplina de Projetos 1 da CESAR School.

| Integrante | E-mail |
|---|---|
| Bruno Soares | bjsm@cesar.school |
| Diógenes Agra | daa3@cesar.school |
| Mariana da Silva | ms4@cesar.school |
| Thiago Felipe | tfss3@cesar.school |

---

# 📚 Contexto Acadêmico

Este projeto foi desenvolvido utilizando conceitos de:
- Design Thinking;
- Modelagem de Dados;
- CRUD;
- Elicitação de Requisitos;
- Prototipação;
- Banco de Dados Relacional.

---

# 📌 Status do Projeto

🚧 Em desenvolvimento
