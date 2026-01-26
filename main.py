import uvicorn

from api.app import app
from fastapi import FastAPI, HTTPException

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
