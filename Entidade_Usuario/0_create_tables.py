import psycopg2


# Establish connection
conn = psycopg2.connect(
host="a465612-akamai-prod-5595182-default.g2a.akamaidb.net",
port=14312,
database="defaultdb",
user="akmadmin",
password="SENHA_AQUI"
)
print("Connection successful")


# Create a cursor object to execute queries
cur = conn.cursor()


# 1. Criação da tabela principal - Usuario
cur.execute("""CREATE TABLE Usuario(
            id_usuario SERIAL PRIMARY KEY,
            nome VARCHAR (100) NOT NULL,
            sobrenome VARCHAR (100) NOT NULL,
            email VARCHAR (150) UNIQUE NOT NULL,
            senha VARCHAR (255) NOT NULL,
            cpf VARCHAR (14) UNIQUE NOT NULL,
            renda NUMERIC (10, 2),
            tipo_moradia VARCHAR (50) NOT NULL);
            """)

print("Table created successfully........")


# 2. Criação da tabela de Endereço (Relação 1:1)
cur.execute("""CREATE TABLE Endereco_Usuario(
    id_usuario INT PRIMARY KEY REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    rua VARCHAR (200),
    numero VARCHAR (20),
    cep VARCHAR (10),
    bairro VARCHAR (100),
    uf CHAR (2),
    complemento VARCHAR (100));
    """)

print("Table Endereco_Usuario created successfully........")

# 3. Criação da tabela de Telefone (Relação 1:N)
cur.execute("""CREATE TABLE Telefone_Usuario(
    id_telefone SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    ddd VARCHAR (3),
    numero VARCHAR (15));
    """)

print(f' Table Telefone created successfully........')



# 4. Criação da tabela de Simulação (Perfil de Consumo)
cur.execute("""CREATE TABLE Simulacao (
    id_simulacao SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    consumo_mensal NUMERIC (10, 2),
    valor_fatura NUMERIC (10, 2),
    economia_estimada NUMERIC (10, 2),
    data_simulacao DATE DEFAULT CURRENT_DATE);
    """)

print(f' Table Simulacao created successfully........')

# Make the changes to the database persistent
conn.commit()

# Close cursor and communication with the database
cur.close()
conn.close()

