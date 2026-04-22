FROM python:3.9-slim
WORKDIR /code
# Instalamos las librerías necesarias
RUN pip install flask redis
COPY app.py .
CMD ["python", "app.py"]
