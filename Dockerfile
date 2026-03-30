FROM python:3.10-slim

WORKDIR /

# Install Runpod SDK
RUN pip install --no-cache-dir runpod

# Copy your handler
COPY handler.py /
CMD ["python", "-u", "/handler.py"]
