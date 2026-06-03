# ☀️ Sol para Todos

Projeto acadêmico desenvolvido na disciplina de **Projetos 1** da CESAR School, com foco na democratização do acesso à energia solar para populações de baixa renda e comunidades com dificuldade de acesso à infraestrutura elétrica.

A aplicação foi desenvolvida em **Python**, com interface via terminal, utilizando **PostgreSQL** como banco de dados relacional.

---

## 🎯 Objetivo

O projeto busca conectar usuários a soluções acessíveis de energia solar, como:

* cooperativas solares;
* energia solar compartilhada;
* financiamento solar;
* programas públicos ou sociais;
* empresas parceiras.

A solução permite que usuários simulem possibilidades de economia, visualizem alternativas disponíveis, encontrem parceiros compatíveis com sua localização e demonstrem interesse em uma solução.

---

## 🧠 Problema

Apesar do crescimento da energia solar no Brasil, grande parte da população ainda enfrenta barreiras para acessar essa tecnologia.

Entre os principais desafios estão:

* alto custo inicial de instalação;
* falta de informação acessível;
* dificuldade de acesso em regiões isoladas;
* desigualdade social e energética;
* ausência de conexão clara entre usuários e soluções viáveis.

---

## 🚀 Tecnologias Utilizadas

### Linguagem

* Python

### Banco de Dados

* PostgreSQL
* SQL puro

### Bibliotecas Python

* psycopg2-binary
* python-dotenv
* bcrypt

### Versionamento

* Git
* GitHub

---

## 🖥️ Tipo de Aplicação

A aplicação é executada via terminal, utilizando menus interativos.

Fluxo geral:

```text
Usuário / Parceiro
↓
Menu interativo no terminal
↓
Python
↓
PostgreSQL
```

Não foi utilizado frontend web, API Flask ou Postman, pois o escopo do projeto foi ajustado para priorizar a implementação do CRUD, a lógica de negócio e a integração com banco de dados relacional.

---

## 📊 Funcionalidades

### Usuário

* Cadastro de usuário;
* Login;
* Visualização de perfil;
* Atualização de perfil;
* Exclusão de conta;
* Cadastro de endereço;
* Cadastro de telefone;
* Realização de simulação;
* Visualização do histórico de simulações;
* Exclusão de simulações;
* Visualização de soluções disponíveis;
* Visualização de parceiros compatíveis por solução e localização;
* Demonstração de interesse em uma solução;
* Visualização dos interesses registrados;
* Cancelamento de interesse.

### Parceiro

* Cadastro de parceiro;
* Login;
* Visualização do perfil da empresa;
* Atualização do perfil da empresa;
* Cadastro de endereço;
* Cadastro de telefone;
* Associação automática com o tipo de solução oferecida;
* Visualização de leads recebidos;
* Atualização do status de leads;
* Cancelamento de leads;
* Exclusão do perfil da empresa.

### Simulação

A simulação recebe:

* consumo mensal em kWh;
* valor médio da fatura de energia.

A aplicação calcula uma estimativa base de economia e exibe uma comparação entre diferentes modelos de solução:

| Solução                     | Estimativa                       |
| --------------------------- | -------------------------------- |
| Cooperativa Solar           | 35% de economia estimada         |
| Energia Solar Compartilhada | 30% de economia estimada         |
| Financiamento Solar         | 10% de economia inicial estimada |
| Programa Público ou Social  | 50% de economia estimada         |

As estimativas são simplificadas e utilizadas apenas para fins de MVP acadêmico.

---

## 🔗 Lógica de Match

O sistema realiza o match entre usuários e parceiros considerando:

1. A solução escolhida pelo usuário;
2. Os parceiros que oferecem aquela solução;
3. A localização do usuário;
4. A localização dos parceiros.

A busca prioriza parceiros da mesma cidade do usuário e, em seguida, parceiros do mesmo estado.

Exemplo:

```text
Usuário: Recife - PE
Solução escolhida: Cooperativa Solar
↓
Sistema busca parceiros que oferecem Cooperativa Solar em PE
↓
Parceiros de Recife aparecem primeiro
```

---

## 🗂️ Modelagem de Banco de Dados

O projeto utiliza banco de dados relacional com as seguintes entidades principais:

* Usuario
* Endereco_Usuario
* Telefone_Usuario
* Simulacao
* Parceiro
* Endereco_Parceiro
* Telefone_Parceiro
* Solucao
* Parceiro_Solucao
* Lead

### Observações de modelagem

* `Usuario` se relaciona com `Simulacao`, `Endereco_Usuario`, `Telefone_Usuario` e `Lead`.
* `Parceiro` se relaciona com `Endereco_Parceiro`, `Telefone_Parceiro`, `Parceiro_Solucao` e `Lead`.
* `Solucao` funciona como catálogo de alternativas disponíveis.
* `Parceiro_Solucao` representa a relação N:N entre parceiros e soluções.
* `Lead` conecta usuário, parceiro e solução.

---

## 🏗️ Estrutura do Projeto

```text
/sol-para-todos
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── /app
│   ├── main.py
│   ├── db.py
│   ├── auth.py
│   │
│   ├── /menus
│   │   ├── menu_principal.py
│   │   ├── menu_usuario.py
│   │   ├── menu_parceiro.py
│   │   ├── opcoes.py
│   │   └── validacoes.py
│   │
│   ├── /services
│   │   ├── usuario_service.py
│   │   ├── parceiro_service.py
│   │   ├── simulacao_service.py
│   │   ├── solucao_service.py
│   │   └── lead_service.py
│   │
│   └── /sql
│       ├── usuario_sql.py
│       ├── parceiro_sql.py
│       ├── simulacao_sql.py
│       ├── solucao_sql.py
│       └── lead_sql.py
│
├── /database
│   ├── schema.sql
│   ├── inserts.sql
│   └── queries.sql
│
└── /docs
    ├── DER.png
    ├── modelo_logico.pdf
    ├── requisitos_funcionais.docx
    └── apresentacao.pdf
```

---

## 📂 Descrição das Pastas

### `/app`

Contém o código principal da aplicação em Python.

### `/app/menus`

Contém os menus interativos exibidos no terminal.

Principais arquivos:

* `menu_principal.py`: menu inicial, login e cadastro;
* `menu_usuario.py`: ações disponíveis para usuários;
* `menu_parceiro.py`: ações disponíveis para parceiros;
* `opcoes.py`: menus fixos de escolha, como tipo de moradia e tipo de serviço;
* `validacoes.py`: validações de entrada, como CPF, CNPJ, DDD, telefone, CEP, UF e e-mail.

### `/app/services`

Contém as regras de negócio da aplicação.

Exemplos:

* criação de usuário;
* autenticação;
* criação de simulação;
* listagem de soluções;
* criação e atualização de leads.

### `/app/sql`

Contém as queries SQL utilizadas pelo Python.

As queries ficam separadas da lógica da aplicação para facilitar manutenção e organização.

### `/database`

Contém os scripts SQL do banco de dados.

* `schema.sql`: criação das tabelas e constraints;
* `inserts.sql`: dados iniciais para teste;
* `queries.sql`: consultas úteis para validação.

### `/docs`

Contém documentos de apoio do projeto, como DER, modelo lógico, requisitos e apresentação.

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-repositorio/sol-para-todos.git
```

### 2. Entrar na pasta do projeto

```bash
cd sol-para-todos
```

### 3. Criar ambiente virtual

```bash
python3 -m venv .venv
```

### 4. Ativar ambiente virtual

```bash
source .venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Criar banco PostgreSQL

Criar um banco chamado:

```text
sol_para_todos
```

### 7. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`.

Exemplo:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sol_para_todos
DB_USER=postgres
DB_PASSWORD=sua_senha
```

O arquivo `.env` não deve ser enviado para o GitHub.

### 8. Executar scripts SQL

Execute os arquivos da pasta `/database` no PostgreSQL:

1. `schema.sql`
2. `inserts.sql`

### 9. Executar aplicação

A partir da raiz do projeto, rode:

```bash
python -m app.main
```

Importante: execute o projeto pela raiz usando `python -m app.main`, e não com `python app/main.py`.

---

## 🔐 Arquivos que não devem ser versionados

Os seguintes arquivos e pastas não devem ser enviados para o GitHub:

```text
.env
.venv/
venv/
__pycache__/
*.pyc
database/backups/
```

O projeto deve manter um `.env.example` com variáveis de exemplo, sem senhas reais.

---

## 🧪 Testes Manuais Recomendados

### Fluxo do usuário

```text
1. Cadastrar usuário
2. Fazer login
3. Visualizar perfil
4. Fazer simulação
5. Visualizar simulações
6. Visualizar soluções disponíveis
7. Escolher solução
8. Visualizar parceiros compatíveis
9. Demonstrar interesse
10. Visualizar interesses
11. Cancelar interesse
```

### Fluxo do parceiro

```text
1. Cadastrar parceiro
2. Fazer login
3. Visualizar perfil da empresa
4. Atualizar perfil
5. Visualizar leads recebidos
6. Atualizar status de lead
7. Cancelar lead
```

### Validações

O sistema valida entradas como:

* CPF com 11 dígitos;
* CNPJ com 14 dígitos;
* DDD com 2 dígitos;
* telefone com 8 ou 9 dígitos;
* CEP com 8 dígitos;
* UF com 2 letras;
* campos obrigatórios;
* renda e valores numéricos não negativos.

---

## 👥 Equipe

Projeto desenvolvido por alunos da disciplina de **Projetos 1** da CESAR School.

| Integrante       | E-mail                                          |
| ---------------- | ----------------------------------------------- |
| Bruno Soares     | [bjsm@cesar.school](mailto:bjsm@cesar.school)   |
| Diógenes Agra    | [daa3@cesar.school](mailto:daa3@cesar.school)   |
| Mariana da Silva | [ms4@cesar.school](mailto:ms4@cesar.school)     |
| Thiago Felipe    | [tfss3@cesar.school](mailto:tfss3@cesar.school) |

---

## 📚 Contexto Acadêmico

Este projeto foi desenvolvido utilizando conceitos de:

* Design Thinking;
* Elicitação de requisitos;
* Prototipação;
* Modelagem de dados;
* DER;
* Modelo lógico;
* CRUD;
* Banco de dados relacional;
* SQL;
* Integração Python com PostgreSQL;
* Versionamento com Git e GitHub.

---

## 📌 Status do Projeto

✅ Finalizado

O projeto foi concluído como entrega acadêmica da disciplina de **Projetos 1**, contemplando modelagem de banco de dados, implementação de CRUD, integração Python com PostgreSQL e execução via terminal.
