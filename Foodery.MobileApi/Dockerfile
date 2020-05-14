FROM python:3.7.4
COPY . /app 
WORKDIR /app

RUN chmod +x start.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_URL 0.0.0.0
ENV FLASK_PORT 5000
EXPOSE 5000

ENTRYPOINT ["/app/start.sh"]