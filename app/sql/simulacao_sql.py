INSERT_SIMULACAO = """
INSERT INTO Simulacao (
    id_usuario,
    consumo_mensal,
    valor_fatura,
    economia_estimada
)
VALUES (%s, %s, %s, %s)
RETURNING id_simulacao;
"""

SELECT_SIMULACOES_POR_USUARIO = """
SELECT
    id_simulacao,
    consumo_mensal,
    valor_fatura,
    economia_estimada,
    TO_CHAR(data_simulacao, 'DD/MM/YYYY "às" HH24:MI')
FROM Simulacao
WHERE id_usuario = %s
ORDER BY data_simulacao DESC;
"""

DELETE_SIMULACAO = """
DELETE FROM Simulacao
WHERE id_simulacao = %s
AND id_usuario = %s;
"""
