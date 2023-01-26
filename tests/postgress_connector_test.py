import configparser
from unittest import TestCase
from src.models.postgres_connector import PostgresConnector

config_file = configparser.ConfigParser()
config_file.read('../config.ini')

base_url = config_file['DOWNLOAD']['base_url']
download_path = config_file['DOWNLOAD']['download_path']

postgres_host = config_file['POSTGRES']['postgres_host']
postgres_database = config_file['POSTGRES']['postgres_database']
postgres_user = config_file['POSTGRES']['postgres_user']
postgres_password = config_file['POSTGRES']['postgres_password']


class TestPostgressConnector(TestCase):

    def setUp(self):
        database = postgres_database
        host = postgres_host
        user = postgres_user
        password = postgres_password
        self.postgres = PostgresConnector(host, database, user, password)

    def test_should_pass_when_fetching_the_database_connection_name(self):
        conn = self.postgres.connect_to_database()
        cursor = conn.cursor()
        cursor.execute("select current_database()")
        db_name = cursor.fetchone()[0]
        conn.close()
        self.assertEqual(self.postgres.database, db_name)

    def test_should(self):
        self.postgres.create_tables()
        conn = self.postgres.connect_to_database()
        cursor = conn.cursor()
        cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables = cursor.fetchall()
        self.assertTrue(len(tables) >= 10)