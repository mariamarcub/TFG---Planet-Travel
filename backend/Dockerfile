# Utiliza una imagen oficial de Python como imagen base
FROM python:3.10-bullseye

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Establece variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE config.settings.production

# Instala dependencias de sistema requeridas
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc build-essential netcat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Actualiza pip
RUN pip install --upgrade pip

# Copia solo el archivo de requisitos al principio para aprovechar la caché de Docker
COPY requirements.txt /app/
# Instala dependencias de Python usando pip
RUN pip install -r requirements.txt

# Después de instalar las dependencias, copia el resto de tu aplicación
COPY . /app/

