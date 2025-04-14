# Technical Interview - Takehome Project

## Objective
Develop a lightweight conversational AI service using Langchain. 
The service should expose at least one API endpoint for chat interactions, 
run a Flask application, and be containerized in Docker. 
A user should be able to ask a question using the endpoint built in Flask, 
and receive an answer from an LLM using Langchain.

## Key Technologies
* Flask
* Langchain / langchain-google-genai - you can get a free Gemini key here: https://aistudio.google.com/apikey
* Docker

## Project Deliverables

### Code Repository:

Well-structured Python project, preferably with folders like:

* app/ (Flask application and routes)

* langchain_integration/ (the chain or AI logic)

* tests/ 

A main script (e.g., app.py) to start the Flask server.

### Dockerfile:

* A Dockerfile that can build the application into a container.

### README File:

Setup instructions, including:

* How to install dependencies locally.

* How to run the application.

* How to build and run the Docker container.

* How to run tests 

### Running the Application with Docker Compose:

1. Ensure you have Docker and Docker Compose installed on your machine.
2. Navigate to the project directory.
3. Run the following command to build and start the containers:
   
   ```bash
   docker-compose up --build
   ```
4. Access the application at `http://localhost:5000`.

5. To stop the application, press `CTRL+C` in the terminal running Docker Compose, or run:
   
   ```bash
   docker-compose down
   ```

Feel free to append to this README file as well so we can easily view the instructions for reference if needed.

##  Interview Prep

During the interview, you will be asked to run the Docker container, answer some basic questions, and receive a response from an LLM. You'll also be asked to explain your code and develop new features during the interview. You are allowed to use an LLM to build the initial project, but you won't be allowed to use one during the interview. 