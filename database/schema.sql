CREATE TABLE Lead (
    id_lead SERIAL PRIMARY KEY,
	id_parceiro INT REFERENCES Parceiro(id_parceiro) ON DELETE CASCADE,
	id_usuario INT REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
	id_solucao INT REFERENCES Solucao(id_solucao) ON DELETE CASCADE,
	status VARCHAR(50) NOT NULL,
	data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Parceiro (
    id_parceiro SERIAL PRIMARY KEY,
	nome_empresa VARCHAR(150) NOT NULL,
	email VARCHAR(150) NOT NULL UNIQUE,
	senha VARCHAR(255) NOT NULL,
	cnpj CHAR(14) NOT NULL UNIQUE,
	tipo_servico VARCHAR(150) NOT NULL
);

CREATE TABLE Solucao (
    id_solucao SERIAL PRIMARY KEY,
	tipo_solucao VARCHAR(150) NOT NULL,
	descricao_solucao TEXT NOT NULL,
	requisitos TEXT NOT NULL
);


CREATE TABLE Endereco_Parceiro (
    id_endereco SERIAL PRIMARY KEY,
    id_parceiro INT UNIQUE REFERENCES Parceiro(id_parceiro) ON DELETE CASCADE,
    rua VARCHAR(150) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    cep VARCHAR(8) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    uf CHAR(2) NOT NULL,
    complemento VARCHAR(100) NULL
);



CREATE TABLE Telefone_Parceiro (
    id_telefone SERIAL PRIMARY KEY,
    id_parceiro INT UNIQUE REFERENCES Parceiro(id_parceiro) ON DELETE CASCADE,
    ddd CHAR(2) NOT NULL,
    numero VARCHAR(9) NOT NULL
);

