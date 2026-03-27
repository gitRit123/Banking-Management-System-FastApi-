FROM python:3.11-slim

WORKDIR /app

# Copy frontend requirements
COPY frontend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend code
COPY frontend/app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
