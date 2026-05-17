-- =========================================
-- SCHEMA REVISADO - SOL PARA TODOS
-- PostgreSQL
-- =========================================

-- =========================================
-- TABELA: Usuario
-- =========================================
CREATE TABLE Usuario (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    renda NUMERIC(10,2) NOT NULL CHECK (renda >= 0),
    tipo_moradia VARCHAR(50) NOT NULL CHECK (
        tipo_moradia IN ('Casa', 'Apartamento', 'Área rural', 'Outro')
    )
);

-- =========================================
-- TABELA: Endereco_Usuario
-- Relação 1:1 com Usuario
-- =========================================
CREATE TABLE Endereco_Usuario (
    id_endereco SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL UNIQUE REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    rua VARCHAR(150) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    complemento VARCHAR(150),
    cep CHAR(8) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL
);

-- =========================================
-- TABELA: Telefone_Usuario
-- Relação 1:N com Usuario
-- =========================================
CREATE TABLE Telefone_Usuario (
    id_telefone SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    ddd CHAR(2) NOT NULL,
    numero VARCHAR(9) NOT NULL
);

-- =========================================
-- TABELA: Simulacao
-- Relação 1:N com Usuario
-- =========================================
CREATE TABLE Simulacao (
    id_simulacao SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    consumo_mensal NUMERIC(10,2) NOT NULL CHECK (consumo_mensal >= 0),
    valor_fatura NUMERIC(10,2) NOT NULL CHECK (valor_fatura >= 0),
    economia_estimada NUMERIC(10,2) NOT NULL CHECK (economia_estimada >= 0),
    data_simulacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================================
-- TABELA: Parceiro
-- =========================================
CREATE TABLE Parceiro (
    id_parceiro SERIAL PRIMARY KEY,
    nome_empresa VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    cnpj CHAR(14) NOT NULL UNIQUE,
    tipo_servico VARCHAR(100) NOT NULL
);

-- =========================================
-- TABELA: Endereco_Parceiro
-- Relação 1:1 com Parceiro
-- =========================================
CREATE TABLE Endereco_Parceiro (
    id_endereco SERIAL PRIMARY KEY,
    id_parceiro INT NOT NULL UNIQUE REFERENCES Parceiro(id_parceiro) ON DELETE CASCADE,
    rua VARCHAR(150) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    complemento VARCHAR(150),
    cep CHAR(8) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL
);

-- =========================================
-- TABELA: Telefone_Parceiro
-- Relação 1:N com Parceiro
-- =========================================
CREATE TABLE Telefone_Parceiro (
    id_telefone SERIAL PRIMARY KEY,
    id_parceiro INT NOT NULL REFERENCES Parceiro(id_parceiro) ON DELETE CASCADE,
    ddd CHAR(2) NOT NULL,
    numero VARCHAR(9) NOT NULL
);

-- =========================================
-- TABELA: Solucao
-- Catálogo de alternativas de acesso
-- =========================================
CREATE TABLE Solucao (
    id_solucao SERIAL PRIMARY KEY,
    tipo_solucao VARCHAR(100) NOT NULL,
    descricao_solucao TEXT NOT NULL,
    requisitos TEXT NOT NULL
);

-- =========================================
-- TABELA: Lead
-- Conecta Usuario, Parceiro e Solucao
-- =========================================
CREATE TABLE Lead (
    id_lead SERIAL PRIMARY KEY,
    id_parceiro INT NOT NULL REFERENCES Parceiro(id_parceiro) ON DELETE CASCADE,
    id_usuario INT NOT NULL REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    id_solucao INT NOT NULL REFERENCES Solucao(id_solucao) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL CHECK (
        status IN ('Novo', 'Em andamento', 'Fechado', 'Cancelado')
    ),
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
