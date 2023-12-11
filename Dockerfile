FROM python:3.9-alpine3.13

WORKDIR /src

COPY requirements.txt .

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3-pip && \
    pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000


CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]


