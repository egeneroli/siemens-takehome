# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose ports
EXPOSE 8000
EXPOSE 8080

# Run the Flask app
# CMD ["python", "src/app/app.py"]
# Run the Flask and Streamlit apps
CMD ["sh", "-c", "python app.py & streamlit run streamlit_chat.py --server.port 8000 && wait"]
