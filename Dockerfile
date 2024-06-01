# Base image olarak Python 3.9-slim kullanıyoruz
FROM python:3.9-slim

# Gerekli bağımlılıkları yüklemek için sistem paketlerini güncelliyoruz ve libmysqlclient-dev paketini kuruyoruz
RUN apt-get update && \
    apt-get install -y build-essential default-libmysqlclient-dev pkg-config

# Çalışma dizinini oluşturup ayarlıyoruz
WORKDIR /code

# requirements.txt dosyasını kopyalıyoruz
COPY requirements.txt /code/

# Gerekli Python paketlerini yüklüyoruz
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Uygulama dosyalarını kopyalıyoruz
COPY . /code/

# Uygulamayı başlatıyoruz
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
