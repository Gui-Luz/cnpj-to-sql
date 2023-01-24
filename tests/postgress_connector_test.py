from unittest import TestCase
from src.models.postgres_connector import PostgresConnector


class TestPostgressConnector(TestCase):

    def setUp(self):
        database = 'CNPJ'
        host = '127.0.0.1'
        user = 'postgres'
        password = 'ALTBsal312512'
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