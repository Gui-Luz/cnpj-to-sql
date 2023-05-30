# CNPJ-TO-SQL

Uma ferramenta para auxiliar o download da base de dados do CNPJ e inserí-la em uma instância Postgres.

### Como usar

1. Clone o repositório.
```bash
git clone https://github.com/Gui-Luz/cnpj-to-sql.git
```
2. Altere o arquivo config.ini com as informações de sua instância postgres.
```text
[POSTGRES]
postgres_host = <endereço da instância>
postgres_database = <base de dados>
postgres_user = <nome de usuário>
postgres_password = <password>
```
#### Rodando com Docker
3. Use o comando docker-compose para subir o container
```bash
docker-compose up
```
#### Rodando localmente
3. Instale as dependências do projeto.
```
pip install -r requirements.txt
```
4. rode o arquivo main.py
```
python -u main.py
```