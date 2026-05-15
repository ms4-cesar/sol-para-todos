import psycopg2

from dotenv import load_dotenv
import os
import psycopg2


# Carrega variáveis do .env
load_dotenv()


# 1. Configurar conexão com o Banco de Dados
def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
   	        port=os.getenv("DB_PORT"),
    	    database=os.getenv("DB_NAME"),
    	    user=os.getenv("DB_USER"),
   	        password=os.getenv("DB_PASSWORD")
        )

        return conn
    except Exception as e:
        return None

# 3. READ (Visualizar Dados do Usuário com JOIN)
def visualizar_usuario(id_usuario):
    conn = get_connection()
    if not conn: return
    
    try:
        cur = conn.cursor()
        # Fazer JOIN para trazer os dados da tabela Usuario, Endereco e Telefone juntos
        query = """
            SELECT u.nome, u.email, u.renda, u.tipo_moradia, e.rua, e.bairro, e.cidade, t.ddd, t.numero
            FROM Usuario u
            LEFT JOIN Endereco_Usuario e ON u.id_usuario = e.id_usuario
            LEFT JOIN Telefone_Usuario t ON u.id_usuario = t.id_usuario
            WHERE u.id_usuario = %s;
        """
        cur.execute(query, (id_usuario,))
        resultado = cur.fetchone()
        
        print(resultado)

        if resultado:
            print("--- DADOS DO USUÁRIO ---")
            print(f"Nome: {resultado[0]} | Email: {resultado[1]} | Renda: R${resultado[2]} | Tipo_Moradia: {resultado[3]}")
            print(f"Endereço: {resultado[3]}, Bairro: {resultado[4]}, Cidade: {resultado[5]}")
            print(f"Telefone: ({resultado[6]}) {resultado[7]}")
        else:
            print("Usuário não encontrado.")
            
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
    finally:
        cur.close()
        conn.close()

visualizar_usuario(5)
