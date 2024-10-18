FROM python:3.8

WORKDIR /app

COPY inference_consumer.py .
COPY requirements_inference.txt .

RUN pip install -r requirements_inference.txt

CMD ["python", "inference_consumer.py"]
