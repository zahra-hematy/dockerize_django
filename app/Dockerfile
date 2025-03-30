FROM python:3.11

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
                  while ! python3 manage.py migrate --noinput ; do sleep 1 ; done && \
                  python3 manage.py collectstatic --noinput && \
                  gunicorn -b 0.0.0.0:8000 upimage.wsgi"]
