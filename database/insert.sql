INSERT na tabela Usuario

INSERT INTO Usuario (
    nome,
    sobrenome,
    email,
    senha,
    cpf,
    renda,
    tipo_moradia
)
VALUES (
    'Thiago',
    'Silva',
    'thiago@email.com',
    'senha123',
    '12345678900',
    5000.00,
    'Própria'
)
RETURNING id_usuario;



#####


INSERT na tabela Endereco_Usuario
INSERT INTO Endereco_Usuario (
    id_usuario,
    rua,
    numero,
    cep,
    bairro,
    cidade,
    uf,
    complemento
)
VALUES (
    1,
    'Rua das Flores',
    '123',
    '50000-000',
    'Centro',
    'Recife',
    'PE',
    'Apartamento 101'
);



#######

INSERT na tabela Telefone_Usuario

INSERT INTO Telefone_Usuario (
    id_usuario,
    ddd,
    numero
)
VALUES (
    1,
    '81',
    '999999999'
);
