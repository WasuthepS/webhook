FROM ubuntu:latest
EXPOSE 5000:5000
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-flask \
    git
RUN git clone https://github.com/WasuthepS/webhook.git


ENV LC_ALL=C.UTF-8   
ENV LANG=C.UTF-8
ENV FLASK_APP=webhook/main.py
RUN flask run --host='0.0.0.0' --port=5000
