FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /django
COPY requirements.txt /django
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /django