FROM python:3.11-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

WORKDIR /app

COPY deployment/requirements.txt /
RUN pip3 install --upgrade pip setuptools && \
    pip3 install --no-cache-dir -r /requirements.txt

COPY . .

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder --chown=django:django /app /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
