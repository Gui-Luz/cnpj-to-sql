import configparser
from unittest import TestCase
from src.models.zip_downloader import ZipDownloader

config_file = configparser.ConfigParser()
config_file.read('../config.ini')

url = config_file['DOWNLOAD']['base_url']
download_path = config_file['DOWNLOAD']['download_path']


class TestCnpjToSql(TestCase):

    def setUp(self):
        base_url = url
        output_path = download_path
        self.cnpj = ZipDownloader(base_url, output_path)

    def test_should_return_true_when_trying_to_request_base_url(self):
        self.cnpj.check_if_base_url_is_valid()
        self.assertTrue(self.cnpj.valid)

    def test_should_return_list_when_getting_zip_files_objects_from_base_url(self):
        self.cnpj.get_zip_objects()
        self.assertEqual(list, type(self.cnpj._zip_objects))
        self.assertIsNotNone(self.cnpj._zip_objects)

    def test_should_return_list_when_getting_files_length_from_base_url(self):
        self.cnpj.get_zip_objects()
        self.cnpj.get_files_length()
        results = True
        for item in self.cnpj.zip_objects:
            if int(item['length']) < 0:
                results = False
        self.assertTrue(results)

    def test_should_return_list_when_getting_downloaded_files_length(self):
        self.cnpj.get_zip_objects()
        self.cnpj.get_files_length()
        self.cnpj.get_downloaded_files_length()
        results = True
        for item in self.cnpj.zip_objects:
            if int(item['downloaded_file_length']) < 0:
                results = False
        self.assertTrue(results)
