# API Project

## Description
This is a FastAPI project with an endpoint that gives you an Email Address, Current datetime in ISO 8601 formatted timestamp, and the GitHub URL.

## Installation (Locally)
    git clone "<https://github.com/edenis00/Public-API-to-Retrieve-Basic-Info>"

Step 2 Create and activate a virtual environment(recommended):
    python -m venv venv
    source venv/bin/activate

Step 3 Install the dependencies:
    pip install -r requirements.txt


## Usage
Step 1 Running the FastAPI project:
    uvicorn main:app --reload


## Endpoint URL
'GET' - '/project'

## Response
status code: 200 ok
body:
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "<https://github.com/yourusername/your-repo>"
}

Step 2 Open your browser and input this URL "http://127.0.0.1:8000/project" to see the output