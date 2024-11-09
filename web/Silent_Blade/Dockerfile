FROM python:2.7-alpine

RUN pip install flask 

COPY ./app /challenge
WORKDIR /challenge

RUN chmod -w -R /challenge

USER nobody

ENV FLASK_APP=app.py

CMD flask run --host=0.0.0.0 --port=1337
