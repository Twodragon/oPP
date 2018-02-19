FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /var/code
COPY requirements.txt /var/code/consumer/
RUN pip install -r /var/code/consumer/requirements.txt
