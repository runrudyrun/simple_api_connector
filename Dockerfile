FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get -y install cron python3

ENV PYTHONPATH "${PYTHONPATH}:/usr/local/lib/python3.9/site-packages"

RUN pip install -r requirements.txt

COPY Connector.py .

COPY Database.py .

COPY Elt.py .

COPY run_elt.py .

RUN chmod +x run_elt.py

COPY crontab /etc/cron.d/elt-cron

RUN chmod 0644 /etc/cron.d/elt-cron

RUN crontab /etc/cron.d/elt-cron

CMD ["cron", "-f"]