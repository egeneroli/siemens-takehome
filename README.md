# Conversational AI Service

## Setup Instructions

### Prerequisites
- Docker
- Python 3.9+

### Local Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd siemens-takehome
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python src/app/app.py
   ```

4. Run the Streamlit UI:
   ```bash
   streamlit run src/streamlit_app.py
   ```

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t conversational-ai-service .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 conversational-ai-service
   ```

### Running Tests
- Tests can be run using a testing framework like pytest. Ensure all tests are located in the `tests/` directory.
