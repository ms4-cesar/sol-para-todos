-- =========================================
-- INSERTS: Usuario
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
('João', 'Silva', 'joao.silva@email.com', 'senha123', '12345678901', 4500.00, 'Apartamento'),
('Maria', 'Oliveira', 'maria.oliveira@email.com', 'senha456', '98765432100', 7200.50, 'Casa'),
('Carlos', 'Souza', 'carlos.souza@email.com', 'senha789', '45678912345', 3200.75, 'Apartamento');

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
(1, 'Rua das Flores', '123', 'Apto 12', '01001000', 'Centro', 'São Paulo', 'SP'),
(2, 'Av Brasil', '456', 'Casa', '22040002', 'Copacabana', 'Rio de Janeiro', 'RJ'),
(3, 'Rua XV de Novembro', '789', NULL, '80020010', 'Centro', 'Curitiba', 'PR');

-- =========================================
-- INSERTS: Telefone_Usuario
-- =========================================
INSERT INTO Telefone_Usuario (
    id_usuario,
    ddd,
    numero
) VALUES
(1, '11', '999999999'),
(1, '11', '988888888'),
(2, '21', '977777777'),
(3, '41', '966666666');

-- =========================================
-- INSERTS: Simulacao
-- =========================================
INSERT INTO Simulacao (
    id_usuario,
    consumo_mensal,
    valor_fatura,
    economia_estimada
) VALUES
(1, 350.50, 420.90, 110.25),
(2, 500.00, 610.30, 180.00),
(3, 275.80, 330.40, 95.75);

-- =========================================
-- INSERTS: Parceiro
-- =========================================
INSERT INTO Parceiro (
    nome_empresa,
    email,
    senha,
    cnpj,
    tipo_servico
) VALUES
('Solar Energy Tech', 'contato@solartech.com', 'solar123', '12345678000199', 'Instalação Solar'),
('Eco Power Solutions', 'vendas@ecopower.com', 'eco456', '98765432000188', 'Consultoria Energética'),
('Green Sun Energia', 'suporte@greensun.com', 'green789', '45612378000177', 'Painéis Fotovoltaicos');

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
(1, 'Rua Energia Solar', '100', 'Galpão A', '13010000', 'Industrial', 'Campinas', 'SP'),
(2, 'Av Sustentável', '2500', NULL, '30140071', 'Savassi', 'Belo Horizonte', 'MG'),
(3, 'Rua Verde', '321', 'Sala 5', '90010000', 'Centro Histórico', 'Porto Alegre', 'RS');

-- =========================================
-- INSERTS: Telefone_Parceiro
-- =========================================
INSERT INTO Telefone_Parceiro (
    id_parceiro,
    ddd,
    numero
) VALUES
(1, '19', '999991111'),
(2, '31', '988882222'),
(3, '51', '977773333');

-- =========================================
-- INSERTS: Solucao
-- =========================================
INSERT INTO Solucao (
    tipo_solucao,
    descricao_solucao,
    requisitos
) VALUES
(
    'Painel Solar Residencial',
    'Sistema de geração de energia solar para residências.',
    'Telhado disponível e boa incidência solar.'
),
(
    'Painel Solar Comercial',
    'Sistema fotovoltaico para empresas de médio porte.',
    'Área mínima de 100m² disponível.'
),
(
    'Consultoria Energética',
    'Análise de consumo e otimização energética.',
    'Envio das últimas 12 faturas de energia.'
);

-- =========================================
-- INSERTS: Lead
-- =========================================
INSERT INTO Lead (
    id_parceiro,
    id_usuario,
    id_solucao,
    status
) VALUES
(1, 1, 1, 'Novo'),
(2, 2, 2, 'Em andamento'),
(3, 3, 3, 'Fechado');
