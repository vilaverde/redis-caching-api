FROM python:3.10-rc-alpine

WORKDIR /usr/share/redis-caching-api

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=app.main.py

CMD ["flask", "run"]
