from db import get_connection
from sql.simulacao_sql import (
    INSERT_SIMULACAO,
    SELECT_SIMULACOES_POR_USUARIO,
    DELETE_SIMULACAO
)


def comparar_solucoes(valor_fatura):
    """
    Compara soluções usando percentuais estimados.
    Essa é uma regra simplificada para o MVP do projeto.
    """

    return [
        {
            "solucao": "Cooperativa Solar",
            "percentual": 0.35,
            "economia": valor_fatura * 0.35,
            "custo_estimado": valor_fatura * 0.65,
            "prazo": "Imediato",
            "observacao": "Não exige instalação própria."
        },
        {
            "solucao": "Energia Solar Compartilhada",
            "percentual": 0.30,
            "economia": valor_fatura * 0.30,
            "custo_estimado": valor_fatura * 0.70,
            "prazo": "Curto prazo",
            "observacao": "Depende da disponibilidade na região."
        },
        {
            "solucao": "Financiamento Solar",
            "percentual": 0.10,
            "economia": valor_fatura * 0.10,
            "custo_estimado": valor_fatura * 0.90,
            "prazo": "3 a 5 anos",
            "observacao": "Economia inicial menor por causa das parcelas."
        },
        {
            "solucao": "Programa Público ou Social",
            "percentual": 0.50,
            "economia": valor_fatura * 0.50,
            "custo_estimado": valor_fatura * 0.50,
            "prazo": "Variável",
            "observacao": "Depende de elegibilidade e disponibilidade do programa."
        }
    ]


def calcular_economia_geral(valor_fatura):
    """
    Economia geral usada apenas para salvar na tabela Simulacao.
    Usamos a média aproximada das alternativas.
    """
    return valor_fatura * 0.30


def criar_simulacao(id_usuario, consumo_mensal, valor_fatura):
    economia_estimada = calcular_economia_geral(valor_fatura)

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            INSERT_SIMULACAO,
            (
                id_usuario,
                consumo_mensal,
                valor_fatura,
                economia_estimada
            )
        )

        id_simulacao = cursor.fetchone()[0]
        conn.commit()

        comparacao = comparar_solucoes(valor_fatura)

        return {
            "id_simulacao": id_simulacao,
            "consumo_mensal": consumo_mensal,
            "valor_fatura": valor_fatura,
            "economia_estimada": economia_estimada,
            "comparacao": comparacao
        }

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()


def listar_simulacoes_usuario(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(SELECT_SIMULACOES_POR_USUARIO, (id_usuario,))
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def excluir_simulacao(id_simulacao, id_usuario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(DELETE_SIMULACAO, (id_simulacao, id_usuario))
        conn.commit()

        return cursor.rowcount > 0

    except Exception as erro:
        conn.rollback()
        raise erro

    finally:
        cursor.close()
        conn.close()
