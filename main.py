import configparser
import os
from src.models.zip_downloader import ZipDownloader
from src.models.postgres_connector import PostgresConnector

config_file = configparser.ConfigParser()
config_file.read(os.path.dirname(__file__) + '/config.ini')

base_url = config_file['DOWNLOAD']['base_url']
download_path = config_file['DOWNLOAD']['download_path']

postgres_host = config_file['POSTGRES']['postgres_host']
postgres_database = config_file['POSTGRES']['postgres_database']
postgres_user = config_file['POSTGRES']['postgres_user']
postgres_password = config_file['POSTGRES']['postgres_password']

if __name__ == '__main__':

    zip = ZipDownloader(base_url, download_path)
    zip.get_zip_objects()
    zip.get_files_length()
    zip.download_zip_files()
    zip.get_downloaded_files_length()
    zip.unzip_files()
    zip.encoding_converter()

    post = PostgresConnector(postgres_host, postgres_database, postgres_user, postgres_password, download_path)
    post.create_tables()
    post.load_postgres()