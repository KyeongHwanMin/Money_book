FROM python:3.9.9

WORKDIR /home/src/

COPY . /home/src/

RUN pip install -r requirements.txt
