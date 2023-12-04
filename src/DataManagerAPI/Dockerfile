FROM python:3.9.6-alpine3.14

WORKDIR /app

COPY ./ /app

RUN pip install -r /app/requirements.txt

CMD sleep 1m; python create_repository.py; python /app/main.py