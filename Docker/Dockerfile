#Base image
FROM python:3.9-slim

#Working directory
WORKDIR /app

#Copy requiremets first (for caching)
COPY requirements.txt .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy application code
COPY . .

#Port
EXPOSE 8000

#command
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
