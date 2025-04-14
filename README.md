# Conversational AI Service

## Setup Instructions

### Prerequisites
- Docker
- Python 3.9+

### Local Setup
Make sure git is installed on your system, and SSH key is configured.
Clone the repository:
   ```bash
   git clone git@github.com:egeneroli/siemens-takehome.git
   ```

### Running the Application with Docker Compose:

To run the application using Docker Compose, follow these steps:

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Navigate to the project directory.
3. Run the following command to build and start the containers:
   
   ```bash
   docker compose up --build
   ```
4. Access the application at `http://localhost:5000`.
5. To stop the application, use `docker compose down`. 

These steps will help you get the application running smoothly in a containerized environment.

### Docker Setup

If you prefer to run the application using standard Docker commands, you can follow these steps:

1. Build the Docker image:
   ```bash
   docker build -t chatbot .
   ```

2. Run the Docker container:
   ```bash
   # run, map ports to expose externally, set environment variable for API key
   docker run -p 8000:8000 -e GOOGLE_API_KEY=$GOOGLE_API_KEY chatbot
   
   # with dev volume to avoid rebuild every time code changes
   docker run -v $(pwd)/src:/app -p 8000:8000 -e GOOGLE_API_KEY=$GOOGLE_API_KEY chatbot
   ```