# Use Python 3.12 slim
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat && rm -rf /var/lib/apt/lists/*

# Copy project code
COPY . .

# Expose Django port
EXPOSE 8000

# Default command
CMD ["gunicorn", "defcon_ecommerce.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "--log-level", "info"]
