INSERT_PARCEIRO = """
INSERT INTO Parceiro (
    nome_empresa,
    email,
    senha,
    cnpj,
    tipo_servico
)
VALUES (%s, %s, %s, %s, %s)
RETURNING id_parceiro;
"""

INSERT_ENDERECO_PARCEIRO = """
INSERT INTO Endereco_Parceiro (
    id_parceiro,
    rua,
    numero,
    complemento,
    cep,
    bairro,
    cidade,
    uf
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""

INSERT_TELEFONE_PARCEIRO = """
INSERT INTO Telefone_Parceiro (
    id_parceiro,
    ddd,
    numero
)
VALUES (%s, %s, %s);
"""

SELECT_PARCEIRO_POR_EMAIL = """
SELECT
    id_parceiro,
    nome_empresa,
    email,
    senha,
    cnpj,
    tipo_servico
FROM Parceiro
WHERE email = %s;
"""

SELECT_PARCEIRO_POR_ID = """
SELECT
    id_parceiro,
    nome_empresa,
    email,
    cnpj,
    tipo_servico
FROM Parceiro
WHERE id_parceiro = %s;
"""

SELECT_ENDERECOS_PARCEIRO = """
SELECT
    id_endereco,
    rua,
    numero,
    complemento,
    cep,
    bairro,
    cidade,
    uf
FROM Endereco_Parceiro
WHERE id_parceiro = %s
ORDER BY id_endereco;
"""

SELECT_TELEFONES_PARCEIRO = """
SELECT
    id_telefone,
    ddd,
    numero
FROM Telefone_Parceiro
WHERE id_parceiro = %s
ORDER BY id_telefone;
"""

UPDATE_PARCEIRO = """
UPDATE Parceiro
SET
    nome_empresa = %s,
    tipo_servico = %s
WHERE id_parceiro = %s;
"""

DELETE_PARCEIRO = """
DELETE FROM Parceiro
WHERE id_parceiro = %s;
"""

SELECT_SOLUCAO_POR_TIPO = """
SELECT id_solucao
FROM Solucao
WHERE tipo_solucao = %s;
"""

INSERT_PARCEIRO_SOLUCAO = """
INSERT INTO Parceiro_Solucao (
    id_parceiro,
    id_solucao
)
VALUES (%s, %s)
ON CONFLICT (id_parceiro, id_solucao) DO NOTHING;
"""