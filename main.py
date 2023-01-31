import configparser
from src.models.zip_downloader import ZipDownloader
from src.models.csv_handler import CsvHandler
from src.models.postgres_connector import PostgresConnector

config_file = configparser.ConfigParser()
config_file.read('./config.ini')

base_url = 'http://200.152.38.155/CNPJ/'
zip_path = './cnpj-zip/'
csv_path = './cnpj-csv/'

postgres_host = config_file['POSTGRES']['postgres_host']
postgres_database = config_file['POSTGRES']['postgres_database']
postgres_user = config_file['POSTGRES']['postgres_user']
postgres_password = config_file['POSTGRES']['postgres_password']

if __name__ == '__main__':

    with open("./logo/logo.ascii", "r") as f:
        art = f.read()
    print(art)

    zd = ZipDownloader(base_url, zip_path, csv_path)
    ch = CsvHandler(zip_path, csv_path)
    pc = PostgresConnector(postgres_host, postgres_database, postgres_user, postgres_password, csv_path)

    zd.check_if_base_url_is_valid()
    pc.connect_to_database()

    zd.get_zip_objects()
    zd.get_files_length()
    zd.get_downloaded_files_length()
    zd.download_zip_files()

    ch.unzip_files()
    ch.encoding_converter()
    ch.remove_null_bytes()

    pc.create_tables()
    pc.load_postgres()
