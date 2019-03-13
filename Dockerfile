ARG ALPINE_VERSION=3.8
ARG PYTHON_VERSION=3.7.2
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

ENV APP_ROOT /app/
ENV FLASK_APP=$APP_ROOT/main.py

RUN mkdir $APP_ROOT
WORKDIR $APP_ROOT

COPY ./requirements.txt $APP_ROOT
RUN pip install -r requirements.txt

COPY . $APP_ROOT

EXPOSE 5000

CMD ["sh", "-e", "entrypoint.sh"]
