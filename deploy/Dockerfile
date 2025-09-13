# Use slim Python base image
FROM python:3.11-slim

# Create nonroot user for safety
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Copy requirements and install deps
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

# Copy application source and config
COPY src/ src/
COPY config/ config/
# Create data directory for host key and logs
RUN mkdir -p data

# Drop privileges
USER appuser

# Run placeholder application
CMD ["python", "-m", "honeypot"]
