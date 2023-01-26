import configparser
import os
from src.models.zip_downloader import ZipDownloader
from src.models.postgres_connector import PostgresConnector
from src.models.csv_handler import CsvHandler
from src.helpers.ascii_printer import ascii_printer

config_file = configparser.ConfigParser()
config_file.read(os.path.dirname(__file__) + '/config.ini')

base_url = config_file['DOWNLOAD']['base_url']
download_path = config_file['DOWNLOAD']['zip_path']
csv_path = config_file['DOWNLOAD']['csv_path']

postgres_host = config_file['POSTGRES']['postgres_host']
postgres_database = config_file['POSTGRES']['postgres_database']
postgres_user = config_file['POSTGRES']['postgres_user']
postgres_password = config_file['POSTGRES']['postgres_password']

if __name__ == '__main__':

    with open("./logo/logo.ascii", "r") as f:
        art = f.read()
    print(art)

    # zip = ZipDownloader(base_url, download_path)
    # zip.get_zip_objects()
    # zip.get_files_length()
    # zip.get_downloaded_files_length()
    # zip.download_zip_files()

    # ch = CsvHandler(download_path, csv_path)
    # ch.unzip_files()
    # ch.encoding_converter()
    # ch.remove_null_bytes()
    #
    # post = PostgresConnector(postgres_host, postgres_database, postgres_user, postgres_password, csv_path)
    # post.create_tables()
    # post.load_postgres()
