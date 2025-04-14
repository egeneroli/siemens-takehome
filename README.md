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

1. Create a `.env` file in the root directory of the project
2. Add the following environment variables:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

You'll need to obtain a Google API key with access to the Gemini model. Never commit your API key to version control.

### Running the Application with Docker Compose:

The application uses Docker Compose with bind mounts for development, which means your local code changes are immediately reflected in the container without requiring rebuilds.

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

The bind mount will ensure your local code changes are immediately reflected in the container. (On most systems, Windows has been known to have issues, for instance.)