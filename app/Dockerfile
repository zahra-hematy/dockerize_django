# FROM python:alpine
# # FROM python:3.11-slim

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SUPERUSER_PASSWORD 12345
# RUN mkdir /app
# WORKDIR /app
# COPY . /app/

# RUN apk update \ 
#     apk add --no-cache gcc gfortran python3-dev musl-dev mariadb-dev 
# RUN pip install  --upgrade pip 
#     #  install -y build-essential python3-dev 

# RUN pip install -r requirements.txt

# CMD python3 manage.py makemigrations --noinput && \ 
#     python3 manage.py migrate --noinput && \
#     python3 manage.py collectstatic --noinput && \
#     gunicorn -b 0.0.0.0:8000 upimage.wsgi

# # # CMD ["sh", "-c", "python3 manage.py makemigrations --noinput && \
# # #                   python3 manage.py migrate --noinput && \
# # #                   python3 manage.py collectstatic --noinput && \
# # #                   python3 manage.py createsuperuser --noinput --username admin --email admin@example.com && \
# # #                   python3 manage.py runserver 0.0.0.0:8000"]
FROM python:3.11-slim-bullseye 
# Install system dependenciesFROM python:3.11-slim-bullseye  # Switch from Alpine to Debian-based image

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1 
# ENV DJANGO_SUPERUSER_PASSWORD=12345

# Create and set work directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run commands
CMD ["sh", "-c", "python3 manage.py makemigrations --noinput && \
                  python3 manage.py migrate --noinput && \
                  python3 manage.py collectstatic --noinput && \
                  gunicorn -b 0.0.0.0:8000 upimage.wsgi"]
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     gcc \
#     python3-dev \
#     default-libmysqlclient-dev \
#     pkg-config && \
#     rm -rf /var/lib/apt/lists/*

# # Environment variables
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1 \
#     DJANGO_SUPERUSER_PASSWORD=12345

# # Create and set work directory
# WORKDIR /app

# # Copy requirements first to leverage Docker cache
# COPY requirements.txt .

# # Install Python dependencies
# RUN pip install --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application
# COPY . .

# # Run commands
# CMD ["sh", "-c", "python3 manage.py makemigrations --noinput && \
#                   python3 manage.py migrate --noinput && \
#                   python3 manage.py collectstatic --noinput && \
#                   gunicorn -b 0.0.0.0:8000 upimage.wsgi"]