FROM python:3.9.0-slim

WORKDIR /UserBehavior

# Copy application code and data
COPY app app
COPY data data
COPY requirements.txt logging.conf ./

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Install system dependencies
RUN apt-get update && \
    apt-get -y install postgresql && \
    apt-get clean

EXPOSE 5001

# Start Gunicorn server with Uvicorn worker
CMD ["gunicorn", "app.main:router", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5001"]
