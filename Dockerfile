# Use an official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy only requirements file first (helps with caching layers)
COPY requirements.txt .

# Install dependencies before copying full project
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Ensure environment variables are loaded
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expose port 5000 for Flask
EXPOSE 5000

# Default command to run the app
CMD ["python", "app.py"]

