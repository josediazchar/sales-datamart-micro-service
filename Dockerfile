
FROM python:3.12

# set work directory /app
WORKDIR /app

# copṕy requirements file to image
COPY requirements.txt .

# install requirements
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# Expose port 8000 for FastAPI API
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
