create_tables_statements = '''
    DROP TABLE if exists cnae;
    CREATE TABLE cnae (
    codigo VARCHAR(7)
    ,descricao VARCHAR(200)
    );
    DROP TABLE if exists empresas;
    CREATE TABLE empresas (
    cnpj_basico VARCHAR(8)
    ,razao_social VARCHAR(200)
    ,natureza_juridica VARCHAR(4)
    ,qualificacao_responsavel VARCHAR(2)
    ,capital_social_str VARCHAR(20)
    ,porte_empresa VARCHAR(2)
    ,ente_federativo_responsavel VARCHAR(50)
    );
    DROP TABLE if exists estabelecimento;
    CREATE TABLE estabelecimento (
    cnpj_basico VARCHAR(8)
    ,cnpj_ordem VARCHAR(4)
    ,cnpj_dv VARCHAR(2)
    ,matriz_filial VARCHAR(1)
    ,nome_fantasia VARCHAR(200)
    ,situacao_cadastral VARCHAR(2)
    ,data_situacao_cadastral VARCHAR(8)
    ,motivo_situacao_cadastral VARCHAR(2)
    ,nome_cidade_exterior VARCHAR(200)
    ,pais VARCHAR(3)
    ,data_inicio_atividades VARCHAR(8)
    ,cnae_fiscal VARCHAR(7)
    ,cnae_fiscal_secundaria VARCHAR(1000)
    ,tipo_logradouro VARCHAR(20)
    ,logradouro VARCHAR(200)
    ,numero VARCHAR(10)
    ,complemento VARCHAR(200)
    ,bairro VARCHAR(200)
    ,cep VARCHAR(8)
    ,uf VARCHAR(2)
    ,municipio VARCHAR(4)
    ,ddd1 VARCHAR(4)
    ,telefone1 VARCHAR(8)
    ,ddd2 VARCHAR(4)
    ,telefone2 VARCHAR(8)
    ,ddd_fax VARCHAR(4)
    ,fax VARCHAR(8)
    ,correio_eletronico VARCHAR(200)
    ,situacao_especial VARCHAR(200)
    ,data_situacao_especial VARCHAR(8)
    );
    DROP TABLE if exists motivo;
    CREATE TABLE motivo (
    codigo VARCHAR(2)
    ,descricao VARCHAR(200)
    );
    DROP TABLE if exists municipio;
    CREATE TABLE municipio (
    codigo VARCHAR(4)
    ,descricao VARCHAR(200)
    );
    DROP TABLE if exists natureza_juridica;
    CREATE TABLE natureza_juridica (
    codigo VARCHAR(4)
    ,descricao VARCHAR(200)
    );
    DROP TABLE if exists pais;
    CREATE TABLE pais (
    codigo VARCHAR(3)
    ,descricao VARCHAR(200)
    );
    DROP TABLE if exists qualificacao_socio;
    CREATE TABLE qualificacao_socio (
    codigo VARCHAR(2)
    ,descricao VARCHAR(200)
    );
    DROP TABLE if exists simples;
    CREATE TABLE simples (
    cnpj_basico VARCHAR(8)
    ,opcao_simples VARCHAR(1)
    ,data_opcao_simples VARCHAR(8)
    ,data_exclusao_simples VARCHAR(8)
    ,opcao_mei VARCHAR(1)
    ,data_opcao_mei VARCHAR(8)
    ,data_exclusao_mei VARCHAR(8)
    );
    DROP TABLE if exists socios_original;
    CREATE TABLE socios_original (
     cnpj_basico VARCHAR(8)
    ,identificador_de_socio VARCHAR(1)
    ,nome_socio VARCHAR(200)
    ,cnpj_cpf_socio VARCHAR(14)
    ,qualificacao_socio VARCHAR(2)
    ,data_entrada_sociedade VARCHAR(8)
    ,pais VARCHAR(3)
    ,representante_legal VARCHAR(11)
    ,nome_representante VARCHAR(200)
    ,qualificacao_representante_legal VARCHAR(2)
    ,faixa_etaria VARCHAR(1)
    )
    '''