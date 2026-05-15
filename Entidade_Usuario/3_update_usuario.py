
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
    

# --- 4. UPDATE (Atualizar Dados - Exemplo atualizando renda e moradia) ---
def atualizar_dados_usuario(id_usuario, nova_renda, novo_tipo_moradia):
    conn = get_connection()
    if not conn: return
    
    try:
        cur = conn.cursor()
        query = """
            UPDATE Usuario
            SET renda = %s, tipo_moradia = %s
            WHERE id_usuario = %s;
        """
        cur.execute(query, (nova_renda, novo_tipo_moradia, id_usuario))
        
        if cur.rowcount > 0:
            conn.commit()
            print(f"Usuário {id_usuario} atualizado com sucesso!")
        else:
            print("Nenhum usuário atualizado. ID pode estar incorreto.")
            
    except Exception as e:
        conn.rollback()
        print(f"Erro ao atualizar: {e}")
    finally:
        cur.close()
        conn.close()


atualizar_dados_usuario(2, 3570.00, 'Proprio')
