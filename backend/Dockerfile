FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu torch

RUN pip install --no-cache-dir -r requirements.txt

#Copy the backend application
COPY . .

EXPOSE 10000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}"]

