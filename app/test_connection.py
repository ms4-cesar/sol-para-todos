from db import get_connection

def testar_conexao():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_usuario, nome, email FROM Usuario;")
        usuarios = cursor.fetchall()

        print("Conexão realizada com sucesso.")
        print("Usuários cadastrados:")

        for usuario in usuarios:
            print(usuario)

        cursor.close()
        conn.close()

    except Exception as erro:
        print("Erro ao conectar no banco:")
        print(erro)

if __name__ == "__main__":
    testar_conexao()
