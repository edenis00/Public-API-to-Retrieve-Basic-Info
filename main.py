from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

current_datetime = datetime.utcnow().isoformat() + "Z"

@app.get("/project")
def index():
    return {
        "Email Address": "edenis0072@gmail.com",
        "Datetime": current_datetime,
    }
