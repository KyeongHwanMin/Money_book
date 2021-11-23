FROM python:3.9.9

WORKDIR /home/src/

COPY . /home/src/

RUN pip install -r requirements.txt

EXPOSE 80880

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]