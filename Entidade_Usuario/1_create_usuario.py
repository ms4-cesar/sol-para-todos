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
    

# 2. CREATE (Criar Usuário, Endereço e Telefone)
def criar_usuario(nome, sobrenome, email, senha, cpf, renda, tipo_moradia, endereco_dict, telefone_dict):
    conn = get_connection()
    if not conn: return

    try:
        cur = conn.cursor()

        # Insere na tabela Usuario e retorna o ID gerado
        query_user = """
            INSERT INTO Usuario (nome, sobrenome, email, senha, cpf, renda, tipo_moradia)
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_usuario;
        """

        cur.execute(query_user, (nome, sobrenome, email, senha, cpf, renda, tipo_moradia))
        id_usuario = cur.fetchone()[0] # Pega o ID gerado


        # Insere na tabela Endereco_Usuario
        query_end = """
            INSERT INTO Endereco_Usuario (id_usuario, rua, numero, cep, bairro, cidade, uf, complemento)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cur.execute(query_end, (
            id_usuario, 
            endereco_dict['rua'], 
            endereco_dict['numero'],
            endereco_dict['cep'], 
            endereco_dict['bairro'],
            endereco_dict['cidade'],
            endereco_dict['uf'], 
            endereco_dict['complemento']))

        # Insere na tabela Telefone_Usuario
        query_tel = """
            INSERT INTO Telefone_Usuario (id_usuario, ddd, numero)
            VALUES (%s, %s, %s);
        """
        cur.execute(query_tel, (id_usuario, telefone_dict['ddd'], telefone_dict['numero']))

        conn.commit() # Confirma as inserções simultaneamente
        print(f'Usuário {nome} criado com sucesso! ID: {id_usuario}')


    except Exception as e:
        conn.rollback() # Desfaz tudo caso algo dê errado
        print(f'Erro ao criar usuário: {e}')
    finally:
        cur.close()
        conn.close()
              

dados_endereco = {
    'rua': 'Rua das Flores', 
    'numero': '123', 
    'cep': '50000-000', 
    'bairro': 'Centro', 
    'uf': 'PE', 
    'complemento': 'Apto 1'
}

dados_telefone = {
    'ddd': '81', 
    'numero': '999998888'
}

print("Iniciando o teste de inserção...")

criar_usuario(
    nome='Carlos',
    sobrenome='Silva',
    email='carlos.silva@exemplo.com',
    senha='user@123', # Num projeto real, isso seria criptografado
    cpf='123.456.789-00',
    renda=2500.00,
    tipo_moradia='Alugada',
    endereco_dict=dados_endereco,
    telefone_dict=dados_telefone
)

