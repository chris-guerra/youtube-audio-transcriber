FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install FFmpeg and dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app /app

# Command to run the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]