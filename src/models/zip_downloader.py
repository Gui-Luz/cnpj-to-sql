import time
import os
import zipfile
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from src.models.downloader import Downloader


class ZipDownloader:

    def __init__(self, base_url, output_path, csv_path):
        self._base_url = base_url
        self._output_path = output_path
        self._csv_path = csv_path
        self._zip_objects = dict()

    def check_if_base_url_is_valid(self):
        print(f'[+] {datetime.now()} Checking base url')
        r = requests.get(self._base_url)
        if r.status_code == 200:
            return True

    def get_zip_objects(self):
        if self.check_if_base_url_is_valid():
            print(f'[+] {datetime.now()} Generating zip objects')
            r = requests.get(self.base_url)
            soup = BeautifulSoup(r.text, 'html.parser')
            for link in soup.find_all('a'):
                if str(link.get('href')).endswith('.zip'):
                    path = link.get('href')
                    if not path.startswith('http'):
                        self.zip_objects[path] = {'name': path, 'url': self.base_url + path}
                    else:
                        self.zip_objects[path] = {'name': path, 'url': path}

    def get_files_length(self):
        if bool(self.zip_objects):
            print(f'[+] {datetime.now()} - Getting files length')
            for key in self.zip_objects.keys():
                url = self.zip_objects[key]['url']
                r = requests.head(url)
                h = r.headers
                self.zip_objects[key]['length'] = int(h['Content-Length'])

    def download_zip_files(self):
        if self.zip_objects:
            print(f'[+] {datetime.now()} STARTING DOWNLOAD')
            start_code = time.monotonic()
            files_for_download = list()
            for key in self.zip_objects.keys():
                if ('download_length' in self.zip_objects[key]) and \
                        (self.zip_objects[key]['length'] == self.zip_objects[key]['download_length']):
                    pass
                else:
                    files_for_download.append(self.zip_objects[key])
            while files_for_download:
                object = files_for_download.pop(0)
                url = object['url']
                file_name = object['name']
                print(f"[+] {datetime.now()} - {len(files_for_download) + 1} - {url}")
                output_path = self._output_path + file_name
                Downloader.download(url, output_path)
            print(f'{(time.monotonic() - start_code) / 60} minutes')

    def get_downloaded_files_length(self):
        print(f'[+] {datetime.now()} Checking downloaded files length')
        for entry in os.scandir(self.output_path):
            if entry.is_file() and entry.name.endswith('.zip'):
                self.zip_objects[entry.name]['download_length'] = entry.stat().st_size


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
