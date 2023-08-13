FROM python:3.11.4-alpine3.17
EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . .