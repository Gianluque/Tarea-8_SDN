FROM python:3.9.2-slim-buster

WORKDIR /app

RUN pip3 install requests

COPY . .

CMD [ "python3","asignacion8.py"]