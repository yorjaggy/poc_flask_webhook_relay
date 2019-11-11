#https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3

FROM python:3.7-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY src /app
WORKDIR /app
CMD ["gunicorn", "--bind 0.0.0.0:80 --workers 2", "main:app"]