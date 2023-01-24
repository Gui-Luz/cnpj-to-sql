import time
import os
import zipfile
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from src.models.downloader import Downloader
from src.models.encoding_converter import EncodingConverter


class ZipDownloader:

    def __init__(self, base_url, output_path):
        self._base_url = base_url
        self._output_path = output_path
        self._zip_objects = list()

    def check_if_base_url_is_valid(self):
        print(f'[+] {datetime.now()} - Checking base url')
        r = requests.get(self._base_url)
        if r.status_code == 200:
            return True

    def get_zip_objects(self):
        if self.check_if_base_url_is_valid():
            print(f'[+] {datetime.now()} - Generating zip objects')
            r = requests.get(self.base_url)
            soup = BeautifulSoup(r.text, 'html.parser')
            for link in soup.find_all('a'):
                if str(link.get('href')).endswith('.zip'):
                    path = link.get('href')
                    if not path.startswith('http'):
                        self.zip_objects.append({'name': path, 'url': self.base_url + path})
                    else:
                        self.zip_objects.append({'name': path, 'url': path})

    def get_files_length(self):
        print(f'[+] {datetime.now()} - Getting files length')
        if self.zip_objects:
            new_objects_list = list()
            length_list = list()
            for obj in self.zip_objects:
                url = obj['url']
                r = requests.head(url)
                h = r.headers
                length_list.append(h['Content-Length'])
            for item in zip(self._zip_objects, length_list):
                old_dict = item[0]
                length = item[1]
                old_dict['length'] = int(length)
                new_objects_list.append(old_dict)
            self.zip_objects = new_objects_list

    def download_zip_files(self):
        if self.zip_objects:
            print(f'[+] {datetime.now()} - STARTING DOWNLOAD')
            start_code = time.monotonic()
            counter = len(self.zip_objects) + 1
            for item in self.zip_objects:
                url = item['url']
                file_name = item['name']
                print(f"[+] {datetime.now()} - {counter} - Downloading {url}")
                output_path = self._output_path + file_name
                Downloader.download(url, output_path)
                counter -= 1
            print(f'{(time.monotonic() - start_code) / 60} minutes')

    def get_downloaded_files_length(self):
        print(f'[+] {datetime.now()} - Checking downloaded files length')
        new_zip_objects = list()
        files_tuples = list()
        for file in os.scandir(self.output_path):
            if file.is_file():
                files_tuples.append((file.name, file.stat().st_size))
        for item in files_tuples:
            for object in self.zip_objects:
                if object['name'] == item[0]:
                    object['downloaded_file_length'] = item[1]
                    new_zip_objects.append(object)
        self.zip_objects = new_zip_objects

    def unzip_files(self):
        for entry in os.scandir(self.output_path):
            if entry.name.endswith('.zip') and not entry.is_dir():
                print(f'[+]  {datetime.now()} - Unzipping ' + entry.name)
                with zipfile.ZipFile(self.output_path + entry.name, 'r') as zip_ref:
                    zip_ref.extractall(self.output_path)

    def encoding_converter(self):
        print(f'[+] {datetime.now()} - STARTING CONVERSION FROM WINDOWS-1252 TO UTF-8')
        start_code = time.monotonic()
        for entry in os.scandir(self.output_path):
            if not entry.name.endswith('.zip') and not entry.name.startswith('.') and not entry.is_dir():
                EncodingConverter.convert(self.output_path + entry.name)
        print(f'{(time.monotonic() - start_code) / 60} minutes')

    @property
    def valid(self):
        return self._valid

    @property
    def zip_objects(self):
        return self._zip_objects

    @zip_objects.setter
    def zip_objects(self, value):
        self._zip_objects = value

    @property
    def base_url(self):
        return self._base_url

    @property
    def output_path(self):
        return self._output_path

