SELECT_SOLUCOES = """
SELECT
    id_solucao,
    tipo_solucao,
    descricao_solucao,
    requisitos
FROM Solucao
ORDER BY id_solucao;
"""

SELECT_SOLUCAO_POR_ID = """
SELECT
    id_solucao,
    tipo_solucao,
    descricao_solucao,
    requisitos
FROM Solucao
WHERE id_solucao = %s;
"""

SELECT_ENDERECO_USUARIO = """
SELECT
    cidade,
    uf
FROM Endereco_Usuario
WHERE id_usuario = %s;
"""

SELECT_PARCEIROS_POR_SOLUCAO_E_LOCALIZACAO = """
SELECT
    p.id_parceiro,
    p.nome_empresa,
    p.email,
    p.tipo_servico,
    ep.cidade,
    ep.uf
FROM Parceiro p
JOIN Parceiro_Solucao ps
    ON p.id_parceiro = ps.id_parceiro
JOIN Endereco_Parceiro ep
    ON p.id_parceiro = ep.id_parceiro
WHERE ps.id_solucao = %s
AND ep.uf = %s
ORDER BY
    CASE
        WHEN ep.cidade = %s THEN 1
        ELSE 2
    END,
    p.nome_empresa;
"""