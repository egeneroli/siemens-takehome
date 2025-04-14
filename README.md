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

### Environment Setup

Before running the application, you need to set up the required environment variables:
1. You'll need to obtain a Google API key with access to the Gemini model. Never commit your API key to version control. You can get a free Gemini key here: https://aistudio.google.com/apikey
2. Create a `.env` file in the root directory of the project
3. Add at least the API key. Feel free to override other defaults like the language model, debug mode, host, and port. Example:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here # required
   DEBUG=True # optional
   LANGUAGE_MODEL=gemini-2.0-flash # optional
   ```



### Running the Application with Docker Compose:
Ensure you have Docker and Docker Compose installed. Recent versions of Docker include docker compose. 
The application uses Docker Compose with bind mounts for development, 
which means your local code changes are immediately reflected in the container without requiring rebuilds. 
(On most systems, Windows has been known to have issues, for instance.)

#### First Time Setup / After Dockerfile Changes

When you first clone the repository or when the Dockerfile / requirements.txt changes, you'll need to build the images:

```bash
docker compose up --build
```

#### Regular Development

For regular development, you can just run:

```bash
docker compose up
```

The bind mount will ensure your local code changes are immediately reflected in the container.

## API Endpoints

### GET /
Returns a welcome message for the chatbot.

### POST /chat
- **Request Body**: JSON with a `prompt` key.
- **Response**: JSON containing the chatbot's response.

### Usage Example

To interact with the chatbot, you can use tools like `curl` or Postman. For example, using `curl`:

```bash
# Send a prompt to the chatbot
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"prompt": "Hello, chatbot!"}'
```

This will return a JSON response with the chatbot's reply.