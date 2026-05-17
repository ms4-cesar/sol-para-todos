INSERT_USUARIO = """
INSERT INTO Usuario (
    nome,
    sobrenome,
    email,
    senha,
    cpf,
    renda,
    tipo_moradia
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
RETURNING id_usuario;
"""

SELECT_USUARIO_POR_EMAIL = """
SELECT
    id_usuario,
    nome,
    sobrenome,
    email,
    senha,
    cpf,
    renda,
    tipo_moradia
FROM Usuario
WHERE email = %s;
"""

SELECT_USUARIO_POR_ID = """
SELECT
    id_usuario,
    nome,
    sobrenome,
    email,
    cpf,
    renda,
    tipo_moradia
FROM Usuario
WHERE id_usuario = %s;
"""

UPDATE_USUARIO = """
UPDATE Usuario
SET
    nome = %s,
    sobrenome = %s,
    renda = %s,
    tipo_moradia = %s
WHERE id_usuario = %s;
"""

DELETE_USUARIO = """
DELETE FROM Usuario
WHERE id_usuario = %s;
"""
