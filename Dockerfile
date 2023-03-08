FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get -y install cron

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY .env .

COPY Connector.py .

COPY Database.py .

COPY Elt.py .

COPY run_elt.py .

RUN chmod +x run_elt.py

COPY crontab /etc/cron.d/elt-cron

RUN chmod 0644 /etc/cron.d/elt-cron

RUN crontab /etc/cron.d/elt-cron

CMD ["cron", "-f"]