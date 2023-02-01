import os
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from src.models.downloader import Downloader
from src.errors.errors import InvalidUrl, EmptyZipObjects


class ZipDownloader:

    def __init__(self, base_url, output_path, csv_path):
        self._base_url = base_url
        self._output_path = output_path
        self._csv_path = csv_path
        self._zip_objects = dict()

    def check_if_base_url_is_valid(self):
        print(f'[+] {datetime.now()} CHECKING BASE URL {self._base_url}')
        r = requests.get(self._base_url)
        if r.status_code == 200:
            return True
        else:
            raise InvalidUrl(f'Invalid base url: {self._base_url}')

    def get_zip_objects(self):
        print(f'[+] {datetime.now()} GENERATING ZIP OBJECTS')
        r = requests.get(self._base_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            if str(link.get('href')).endswith('.zip'):
                path = link.get('href')
                if not path.startswith('http'):
                    self._zip_objects[path] = {'name': path, 'url': self._base_url + path}
                else:
                    self._zip_objects[path] = {'name': path, 'url': path}

    def get_files_length(self):
        if bool(self._zip_objects):
            print(f'[+] {datetime.now()} GETTING FILES LENGTH')
            for key in self._zip_objects.keys():
                url = self._zip_objects[key]['url']
                r = requests.head(url)
                h = r.headers
                self._zip_objects[key]['length'] = int(h['Content-Length'])
        else:
            raise EmptyZipObjects("You did not call the 'get_zip_objects' method before calling this method.")

    def download_zip_files(self):
        if self._zip_objects:
            print(f'[+] {datetime.now()} STARTING DOWNLOAD')
            files_for_download = list()
            for key in self._zip_objects.keys():
                if ('download_length' in self._zip_objects[key]) and \
                        (self._zip_objects[key]['length'] == self._zip_objects[key]['download_length']):
                    pass
                else:
                    files_for_download.append(self._zip_objects[key])
            while files_for_download:
                obj = files_for_download.pop(0)
                url = obj['url']
                file_name = obj['name']
                print(f"[+] {datetime.now()} - {len(files_for_download) + 1} - {url}")
                output_path = self._output_path + file_name
                Downloader.download(url, output_path)

    def get_downloaded_files_length(self):
        print(f'[+] {datetime.now()} CHECKING DOWNLOADED FILES LENGTH')
        for entry in os.scandir(self._output_path):
            if entry.is_file() and entry.name.endswith('.zip'):
                self._zip_objects[entry.name]['download_length'] = entry.stat().st_size
