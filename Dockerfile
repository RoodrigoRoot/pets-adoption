FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir /var/log/pets
RUN chmod 777 /var/log/pets

RUN mkdir /pets
WORKDIR /pets

COPY . .

RUN pip install -r requirements.txt

