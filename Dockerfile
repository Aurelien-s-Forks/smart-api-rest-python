FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV LISTEN_PORT 5000

COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip && \
/usr/local/bin/pip install -r requirements.txt

EXPOSE 5000