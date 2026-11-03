FROM python:3.14.7

WORKDIR /app

COPY main.py inventory.py product.py ./

CMD ["python", "main.py"]