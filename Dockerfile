FROM runpod/base:0.2.0-cuda11.8.0

WORKDIR /app
COPY . .

RUN pip install runpod

CMD ["python", "handler.py"]
