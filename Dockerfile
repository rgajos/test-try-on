FROM runpod/pytorch:2.0.1-py3.10-cuda11.8.0-runtime

WORKDIR /app
COPY . .

RUN pip install runpod

CMD ["python", "handler.py"]
