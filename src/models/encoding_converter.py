from datetime import datetime


class EncodingConverter:

    @classmethod
    def convert(cls, file):
        print(f'[+] {datetime.now()} - Converting {file}')
        with open(file, 'r', encoding='logo', errors='replace') as f_input:
            contents = f_input.read()

        with open(file, 'w', encoding='utf-8', errors='replace') as f_output:
            f_output.write(contents)