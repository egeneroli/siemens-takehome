# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt --default-timeout=100

# Copy the current directory contents into the container at /app
COPY src .

# Expose port
EXPOSE 8080

# Run the Flask app
CMD ["python", "-m", "main"]
