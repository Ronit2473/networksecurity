# Network Intrusion Prediction System: Scalable MLOps Pipeline

**Author:** Ronit Singha Roy

## Project Overview
This repository contains the source code for an end-to-end Scalable MLOps Pipeline designed for real-time network intrusion detection and network security analysis (specifically targeting phishing data). The system automates model training cycles, manages batch data ingestion, and deploys a predictive modeling API to continuously monitor network safety.

## Key Features
* **Automated MLOps Workflow:** Complete preprocessing pipeline that automates model training and evaluation cycles using GitHub Actions.
* **FastAPI Predictive API:** A high-performance, real-time inference API built with FastAPI, enabling seamless integration with interactive front-end reporting templates (HTML/Jinja2).
* **Batch Data Ingestion:** Automated handling of network security data (CSV format) for robust model training.
* **Database Integration:** Comprehensive system monitoring, data storage, and logging using MongoDB to track performance and manage model versioning.
* **Dockerized Deployment:** Containerized application environment for scalable, consistent, and easy deployment across different cloud infrastructures.

## Tech Stack
* **Language:** Python 3.x
* **Framework:** FastAPI (Backend / API creation)
* **Database:** MongoDB (`pymongo`)
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Frontend Integration:** HTML, Jinja2 (served via FastAPI `templates/`)
* **DevOps/MLOps:** Docker, GitHub Actions, `setup.py` for packaging

## Project Structure
```
networksecurity/
├── .github/workflows/   # CI/CD and MLOps automation pipelines
├── networksecurity/     # Main Python package (ML pipeline, components, config)
├── data_schema/         # Schema validation definitions
├── final_model/         # Saved serialized machine learning models
├── network_data/        # Raw and processed network dataset storage
├── prediction_output/   # Generated batch inference results
├── templates/           # HTML/Jinja2 templates for the web interface
├── valid_data/          # Validated data batches ready for training
├── app.py               # FastAPI application entry point
├── main.py              # ML pipeline execution script
├── push_data.py         # Script to ingest/push data to MongoDB
├── test_mongo.py        # MongoDB connection testing script
├── Dockerfile           # Docker image configuration
├── requirements.txt     # Python dependencies
└── setup.py             # Package configuration
```

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Ronit2473/networksecurity.git
cd networksecurity
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory to store your MongoDB connection string:
```
MONGO_DB_URL=your_mongodb_connection_string
```

### 4. Running the Application
You can start the FastAPI server using the following command:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
Alternatively, if using Docker:
```bash
docker build -t network-security-app .
docker run -p 8000:8000 network-security-app
```

## Usage
Once the API is running, you can:
1. Navigate to `http://localhost:8000/` to view the frontend web interface.
2. Navigate to `http://localhost:8000/docs` to interact with the auto-generated Swagger UI for testing API endpoints (e.g., triggering training pipelines or running predictions).
3. Use `python main.py` to manually trigger the model training pipeline.

