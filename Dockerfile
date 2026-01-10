# Gunakan image Python 3.11-slim
FROM python:3.11-slim

# Mencegah Python menulis file .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Direktori kerja di dalam kontainer
WORKDIR /app

# INSTAL DEPENDENSI SISTEM UNTUK MYSQL
# Kita butuh build-essential dan library mysql agar mysqlclient bisa terinstal
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instal library Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua kode proyek ke kontainer
COPY . /app/

# Perintah untuk menjalankan Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]