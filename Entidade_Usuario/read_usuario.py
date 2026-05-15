import psycopg2

# 1. Configurar conexão com o Banco de Dados
def get_connection():
    try:
        conn = psycopg2.connect(
            host="a465612-akamai-prod-5595182-default.g2a.akamaidb.net",
            port=14312,
            database="defaultdb",
            user="akmadmin",
	    password="SENHA_AQUI"
        )
        return conn
    except Exception as e:
        return None
    

# Teste rápido para ver os usuários cadastrados
conn = get_connection()
cur = conn.cursor()

print("\n--- VALIDANDO O BANCO DE DADOS ---")
cur.execute("SELECT id_usuario, nome, cpf FROM Usuario;")
usuarios = cur.fetchall() # Pega todas as linhas retornadas

if usuarios:
    for u in usuarios:
        print(f"Encontrado -> ID: {u[0]} | Nome: {u[1]} | CPF: {u[2]}")
else:
    print("Nenhum usuário encontrado na tabela.")

cur.close()
conn.close()
