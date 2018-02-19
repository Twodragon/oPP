FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /var/code
COPY requirements.txt /var/code/producer/
RUN pip install -r /var/code/producer/requirements.txt
