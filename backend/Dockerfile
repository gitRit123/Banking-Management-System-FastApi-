# 1. Base image
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy backend requirements
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy ALL backend files (current directory)
COPY . .

# 6. Expose FastAPI port
EXPOSE 8000

# 7. Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
