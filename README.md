# CNPJ-TO-SQL

Uma ferramenta para auxiliar o download da base de dados do CNPJ e inseri-la em uma instância Postgres.

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
3. Construa a imagem docker.
```bash
make build
```
4. Rode o container.
```bash
make run
```
