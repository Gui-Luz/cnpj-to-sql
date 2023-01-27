import os
from datetime import datetime
import psycopg2
from src.helpers.sql_statements import create_tables_statements
from src.helpers.table_name_mapping import table_name_mapping
from src.helpers.summary_statement import summary_statement


class PostgresConnector:

    def __init__(self, host, database, user, password, csv_folder):
        self._host = host
        self._database = database
        self._user = user
        self._password = password
        self._csv_folder = csv_folder

    def connect_to_database(self):
        conn = psycopg2.connect(database=self.database, host=self.host, user=self.user, password=self.password)
        return conn

    def create_tables(self):
        statements = [s.strip() for s in create_tables_statements.split(';')]
        conn = self.connect_to_database()
        cursor = conn.cursor()
        for statement in statements:
            cursor.execute(statement)
        conn.commit()
        conn.close()

    def load_postgres(self):
        print(f'[+] {datetime.now()} STARTING SQL LOADING')
        conn = self.connect_to_database()
        cursor = conn.cursor()
        for entry in os.scandir(self.csv_folder):
            if not entry.name.endswith('.zip') and not entry.name.startswith('.') and not entry.is_dir():
                table_name = entry.name.rsplit('.', 1)[1]
                if 'SIMPLES' in entry.name:
                    table_name = 'simples'
                print(f'[+] {datetime.now()} - Loading {entry.name} into {table_name_mapping[table_name]} table')
                with open(self.csv_folder + entry.name, 'r', encoding='utf-8') as f:
                    cursor.copy_expert(f"COPY {table_name_mapping[table_name]} FROM STDIN WITH (FORMAT CSV, HEADER "
                                   f"false, DELIMITER ';')", f)
                conn.commit()
        cursor.close()
        conn.close()

    def get_database_summary(self):
        print(f'[+] {datetime.now()} DATABASE SUMMARY:')
        conn = self.connect_to_database()
        cursor = conn.cursor()
        cursor.execute(summary_statement)
        summary = cursor.fetchall()
        for table in summary:
            schema = table[0]
            table_name = table[1]
            rows = table[2]
            print(f'[+] {schema}.{table_name} | {int(rows)} rows')

    @property
    def host(self):
        return self._host

    @property
    def database(self):
        return self._database

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def csv_folder(self):
        return self._csv_folder