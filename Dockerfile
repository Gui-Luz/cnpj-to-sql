FROM python:3.9-alpine

COPY main.py /app/
COPY requirements.txt /app/
COPY config.ini /app/
COPY src /app/src/
COPY logo /app/logo/

WORKDIR /app/

RUN pip install -r requirements.txt
RUN mkdir cnpj-zip
RUN mkdir cnpj-csv

ENTRYPOINT ["python", "-u", "main.py"]
