-- =========================================
-- INSERTS COERENTES - SOL PARA TODOS
-- PostgreSQL
-- =========================================

-- =========================================
-- INSERTS: Usuario
-- Perfis alinhados ao problema do projeto:
-- baixa renda, área rural, classe média baixa
-- =========================================

INSERT INTO Usuario (
    nome,
    sobrenome,
    email,
    senha,
    cpf,
    renda,
    tipo_moradia
) VALUES
(
    'Maria',
    'Santos',
    'maria.santos@email.com',
    'senha123',
    '12345678901',
    1800.00,
    'Casa'
),
(
    'José',
    'Oliveira',
    'jose.oliveira@email.com',
    'senha456',
    '98765432100',
    1200.00,
    'Área rural'
),
(
    'Ana',
    'Pereira',
    'ana.pereira@email.com',
    'senha789',
    '45678912345',
    2800.00,
    'Apartamento'
),
(
    'Carlos',
    'Lima',
    'carlos.lima@email.com',
    'senha321',
    '32165498700',
    2200.00,
    'Casa'
);

-- =========================================
-- INSERTS: Endereco_Usuario
-- =========================================

INSERT INTO Endereco_Usuario (
    id_usuario,
    rua,
    numero,
    complemento,
    cep,
    bairro,
    cidade,
    uf
) VALUES
(
    1,
    'Rua Nova Esperança',
    '120',
    NULL,
    '50000001',
    'Ibura',
    'Recife',
    'PE'
),
(
    2,
    'Sítio Boa Vista',
    'S/N',
    NULL,
    '55000002',
    'Zona Rural',
    'Caruaru',
    'PE'
),
(
    3,
    'Avenida Norte',
    '450',
    'Apto 203',
    '52000003',
    'Casa Amarela',
    'Recife',
    'PE'
),
(
    4,
    'Rua do Sol',
    '88',
    NULL,
    '53000004',
    'Peixinhos',
    'Olinda',
    'PE'
);

-- =========================================
-- INSERTS: Telefone_Usuario
-- =========================================

INSERT INTO Telefone_Usuario (
    id_usuario,
    ddd,
    numero
) VALUES
(1, '81', '999111222'),
(2, '81', '988222333'),
(3, '81', '977333444'),
(4, '81', '966444555');

-- =========================================
-- INSERTS: Simulacao
-- Simulações com contas compatíveis com baixa/média renda
-- =========================================

INSERT INTO Simulacao (
    id_usuario,
    consumo_mensal,
    valor_fatura,
    economia_estimada
) VALUES
(
    1,
    180.00,
    165.00,
    55.00
),
(
    2,
    120.00,
    110.00,
    40.00
),
(
    3,
    240.00,
    230.00,
    75.00
),
(
    4,
    200.00,
    190.00,
    65.00
);

-- =========================================
-- INSERTS: Parceiro
-- Parceiros alinhados com soluções acessíveis
-- =========================================

INSERT INTO Parceiro (
    nome_empresa,
    email,
    senha,
    cnpj,
    tipo_servico
) VALUES
(
    'Cooperativa Solar Recife',
    'contato@cooperativasolarrecife.com',
    'coop123',
    '12345678000199',
    'Cooperativa Solar'
),
(
    'Energia Compartilhada Nordeste',
    'atendimento@energianordeste.com',
    'energia456',
    '98765432000188',
    'Energia Solar Compartilhada'
),
(
    'Banco Solar Popular',
    'contato@bancosolarpopular.com',
    'banco789',
    '45612378000177',
    'Financiamento Solar'
),
(
    'Programa Luz Solar Social',
    'programa@luzsolarsocial.org',
    'social321',
    '32198765000155',
    'Programa Público'
);

-- =========================================
-- INSERTS: Endereco_Parceiro
-- =========================================

INSERT INTO Endereco_Parceiro (
    id_parceiro,
    rua,
    numero,
    complemento,
    cep,
    bairro,
    cidade,
    uf
) VALUES
(
    1,
    'Rua da Sustentabilidade',
    '100',
    'Sala 01',
    '50010000',
    'Boa Vista',
    'Recife',
    'PE'
),
(
    2,
    'Avenida Energia Limpa',
    '250',
    NULL,
    '51020000',
    'Pina',
    'Recife',
    'PE'
),
(
    3,
    'Rua do Crédito Verde',
    '300',
    'Sala 12',
    '52030000',
    'Espinheiro',
    'Recife',
    'PE'
),
(
    4,
    'Avenida Social',
    '50',
    NULL,
    '53040000',
    'Centro',
    'Olinda',
    'PE'
);

-- =========================================
-- INSERTS: Telefone_Parceiro
-- =========================================

INSERT INTO Telefone_Parceiro (
    id_parceiro,
    ddd,
    numero
) VALUES
(1, '81', '999555111'),
(2, '81', '988555222'),
(3, '81', '977555333'),
(4, '81', '966555444');

-- =========================================
-- INSERTS: Solucao
-- Catálogo coerente com democratização do acesso
-- =========================================

INSERT INTO Solucao (
    tipo_solucao,
    descricao_solucao,
    requisitos
) VALUES
(
    'Cooperativa Solar',
    'Modelo em que usuários participam de uma geração compartilhada de energia solar, sem precisar instalar painéis na própria residência.',
    'Disponibilidade de cooperativa ativa na região e cadastro aprovado.'
),
(
    'Energia Solar Compartilhada',
    'Modelo em que o usuário recebe créditos na conta de energia a partir de uma usina solar remota.',
    'Residência conectada à rede elétrica e disponibilidade do serviço na região.'
),
(
    'Financiamento Solar',
    'Alternativa para parcelar a instalação de um sistema solar residencial.',
    'Análise de crédito, renda compatível e imóvel com estrutura adequada.'
),
(
    'Programa Público ou Social',
    'Iniciativa pública ou social voltada à ampliação do acesso à energia solar para populações de baixa renda.',
    'Atender aos critérios socioeconômicos definidos pelo programa.'
);

-- =========================================
-- INSERTS: Lead
-- Conexões entre usuários, soluções e parceiros
-- =========================================

INSERT INTO Lead (
    id_parceiro,
    id_usuario,
    id_solucao,
    status
) VALUES
(
    1,
    1,
    1,
    'Novo'
),
(
    2,
    2,
    2,
    'Em andamento'
),
(
    3,
    3,
    3,
    'Novo'
),
(
    4,
    4,
    4,
    'Fechado'
);
