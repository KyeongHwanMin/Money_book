FROM python:3.9.9

WORKDIR /home/src/

COPY . /home/src/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", " --settings config.settings_docker", "0.0.0.0:8080"]
