# Python bazaviy imidj
FROM python:3.10-slim

# Ishchi katalog
WORKDIR /app

# System kutubxonalarini o'rnatish
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Talablar faylini ko'chirish va o'rnatish
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini ko‘chirish
COPY . .

# Django migration va serverni ishga tushirish buyruqlari
CMD ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]
