import os
from datetime import datetime
import zipfile
from src.models.encoding_converter import EncodingConverter
from src.models.null_bytes_remover import NullBytesRemover


class CsvHandler:

    def __init__(self, zip_path, csv_path):
        self._zip_path = zip_path
        self._csv_path = csv_path

    def unzip_files(self):
        for entry in os.scandir(self._zip_path):
            if entry.name.endswith('.zip') and not entry.is_dir():
                print(f'[+] {datetime.now()} Unzipping ' + entry.name)
                with zipfile.ZipFile(self._zip_path + entry.name, 'r') as zip_ref:
                    zip_ref.extractall(self._csv_path)

    def encoding_converter(self):
        print(f'[+] {datetime.now()} STARTING CONVERSION FROM LATIN-1 TO UTF-8')
        for entry in os.scandir(self._csv_path):
            if not entry.name.endswith('.zip') and not entry.name.startswith('.') and not entry.is_dir():
                EncodingConverter.convert(self._csv_path + entry.name)

    def remove_null_bytes(self):
        print(f'[+] {datetime.now()} REMOVING NULL BYTES')
        for entry in os.scandir(self._csv_path):
            if not entry.name.endswith('.zip') and not entry.name.startswith('.') and not entry.is_dir():
                NullBytesRemover.remove(self._csv_path + entry.name)
