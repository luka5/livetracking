FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

USER 1000

ENTRYPOINT ["python"]
CMD ["app.py"]
