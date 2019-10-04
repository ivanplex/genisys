# https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99
FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /genisys
ADD ./requirements.txt	/genisys/requirements.txt
RUN pip install -r requirements.txt
COPY . /genisys/

CMD ["gunicorn", "-w 2", "-b 0.0.0.0", "genisys.wsgi"]
EXPOSE 8080
