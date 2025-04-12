# Siemens Takehome Challenge

## Setup Instructions

### Install Dependencies
Run the following command to install the required dependencies:
```
pip install -r requirements.txt
```

### Run the Application
To run the Flask application, execute:
```
python -m flask run
```

### Build and Run the Docker Container
To build the Docker container, run:
```
docker build -t siemens-takehome .
```

Then, run the container:
```
docker run -p 5000:5000 siemens-takehome
```

### Run Tests
To run the tests, execute:
```
python -m unittest discover -s tests
```
