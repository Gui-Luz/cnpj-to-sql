from datetime import datetime


class EncodingConverter:

    @classmethod
    def convert(cls, file):
        print(f'[+] {datetime.now()} - Converting {file}')
        with open(file, 'r', encoding='windows-1252') as f_input:
            contents = f_input.read()

        with open(file, 'w', encoding='utf-8', errors='ignore') as f_output:
            f_output.write(contents)