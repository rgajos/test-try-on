FROM runpod/worker:latest

WORKDIR /app
COPY . .

RUN pip install runpod

CMD ["python", "handler.py"]
