# Use the official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Flask listens on port 5000
EXPOSE 5000

# Start the application
CMD ["python", "run.py"]
