from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/project", status_code=200)
def index():
    current_datetime = datetime.utcnow().isoformat() + "Z"
    return JSONResponse(
        status_code=200,
        content={
            "Email Address": "edenis0072@gmail.com",
            "Datetime": current_datetime,
            "Github Repo": "<https://github.com/edenis00/Public-API-to-Retrieve-Basic-Info>",
        },
    )
