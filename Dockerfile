# syntax = docker/dockerfile:1.6

FROM python:3.12-alpine3.20 AS main
RUN apk --no-cache add curl
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py utils.py ./

EXPOSE 10000
CMD [ "python", "bot.py" ]
