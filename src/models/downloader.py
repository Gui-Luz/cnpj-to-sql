import requests
from tqdm import tqdm


class Downloader:

    @classmethod
    def download(cls, url, file_path):
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        with open(file_path, 'wb') as f:
            for data in tqdm(response.iter_content(block_size), total=total_size/block_size, unit='MB', unit_scale=True):
                f.write(data)