# syntax=docker/dockerfile:1

FROM python:3.11.4
RUN pip install --upgrade pip

WORKDIR /watertower

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src/

ENV PYTHONPATH="${PYTHONPATH}:/watertower/"

CMD ["python", "src/webserver/webserver.py"]