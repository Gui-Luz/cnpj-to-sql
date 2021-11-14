# cnpj-mysql
Script em python para carregar os arquivos de cnpj dos dados públicos da Receita Federal em MYSQL.

## Dados públicos de cnpj no site da Receita:
A partir de 2021 os dados da Receita Federal estão disponíveis no link https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj (ou http://200.152.38.155/CNPJ/) em formato csv zipado. 

## Pré-requisitos:
Python 3.8;<br>
Bibliotecas pandas, dask, sqlalchemy e pymysql.<br>

## Utilizando o script:
Baixe todos os arquivos zipados do site da Receita e salve na pasta "dados-publicos-zip".<br>
O download no site da Receita é lento, pode demorar várias horas. Sugiro utilizar um gerenciador de downloads.<br><br>
Crie uma pasta com o nome "dados-publicos".<br>

No servidor MYSQL, crie um database, por exemplo, cnpj.<br>
Especifique os parâmetros no começo do script:<br>
dbname = 'cnpj'<br>
username = 'root'<br>
password = ''<br>
host = '127.0.0.1'<br>

Para iniciar esse script, em um console DOS digite<br>
python dados_cnpj_para_mysql.py<br>

A execução durou cerca de 5hs em um notebook i7 de 8a geração.

## Outras referências:

Para trabalhar com os dados de cnpj no formato SQLITE, use o meu projeto (https://github.com/rictom/cnpj-sqlite).<br>
O projeto (https://github.com/rictom/rede-cnpj) utiliza os dados públicos de CNPJ para visualização de relacionamentos entre empresas e sócios.<br>

## Histórico de versões

versão 0.1 (novembro/2021)
- primeira versão
