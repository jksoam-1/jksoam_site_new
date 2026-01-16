FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# -------------------------------
# Install ONLY runtime deps
# -------------------------------
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libpq5 \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------
# Python deps
# -------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip

# -------------------------------
# Copy project
# -------------------------------
COPY django_site /app/django_site

WORKDIR /app/django_site

# -------------------------------
# Collect static
# -------------------------------
RUN python manage.py collectstatic --noinput

EXPOSE 8000
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "django_site.wsgi:application", "--bind", "0.0.0.0:8000"]
