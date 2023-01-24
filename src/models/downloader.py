import requests
import shutil


class Downloader:

    @classmethod
    def download(cls, url, file_path):
        r = requests.get(url, stream=True)
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
