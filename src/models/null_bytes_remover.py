from datetime import datetime


class NullBytesRemover:

    @classmethod
    def remove(cls, file):
        print(f'[+] {datetime.now()} - Removing from {file}')
        with open(file, "rb") as f:
            data = f.read()
        data = data.replace(b'\x00', b'')
        with open(file, "wb") as f:
            f.write(data)
