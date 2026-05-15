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
     
# =======================================================
# MENU INTERATIVO: CADASTRANDO USUÁRIO VIA TERMINAL
# =======================================================

print("========================================")
print("   BEM-VINDO AO APP SOL PARA TODOS      ")
print("========================================")
print("Por favor, preencha os dados abaixo para criar sua conta.\n")

# 1. Coletando os Dados Pessoais
print("--- DADOS PESSOAIS ---")
nome_input = input("Nome: ")
sobrenome_input = input("Sobrenome: ")
email_input = input("E-mail: ")
senha_input = input("Senha: ")
cpf_input = input("CPF (ex: 123.456.789-00): ")

# Tratamento simples para garantir que a renda seja salva como número decimal (float)
renda_str = input("Renda Mensal em R$ (ex: 1500.50): ")
try:
    # Substitui vírgula por ponto caso o usuário digite no padrão brasileiro
    renda_input = float(renda_str.replace(',', '.')) 
except ValueError:
    print("Valor de renda inválido. Definindo como 0.0 por padrão.")
    renda_input = 0.0

tipo_moradia_input = input("Tipo de Moradia (ex: Própria, Alugada): ")


# 2. Coletando os Dados de Endereço
print("\n--- DADOS DE ENDEREÇO ---")
rua_input = input("Rua: ")
numero_input = input("Número: ")
cep_input = input("CEP (ex: 50000-000): ")
bairro_input = input("Bairro: ")
cidade_input = input("Cidade: ")
uf_input = input("UF (ex: PE): ")
complemento_input = input("Complemento: ")

# Montando o dicionário de endereço com os dados digitados
dados_endereco = {
    'rua': rua_input,
    'numero': numero_input,
    'cep': cep_input,
    'bairro': bairro_input,
    'cidade': cidade_input,
    'uf': uf_input,
    'complemento': complemento_input
}


# 3. Coletando os Dados de Contato
print("\n--- TELEFONE DE CONTATO ---")
ddd_input = input("DDD (ex: 81): ")
numero_tel_input = input("Número (ex: 988887777): ")

# Montando o dicionário de telefone
dados_telefone = {
    'ddd': ddd_input,
    'numero': numero_tel_input
}


# 4. Enviando tudo para o Banco de Dados
print("\nProcessando cadastro... Conectando ao banco de dados...")

# Aqui chamamos a função que você já tinha criado, passando as variáveis que acabamos de preencher!
criar_usuario(
    nome=nome_input,
    sobrenome=sobrenome_input,
    email=email_input,
    senha=senha_input,
    cpf=cpf_input,
    renda=renda_input,
    tipo_moradia=tipo_moradia_input,
    endereco_dict=dados_endereco,
    telefone_dict=dados_telefone
)

print("\nFim do processo.")
