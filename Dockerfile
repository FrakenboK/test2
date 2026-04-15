FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache docker-cli

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]