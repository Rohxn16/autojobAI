from fastapi import FastAPI, HTTPException
from api.resume_uploader.resume_upload import  router as resume_uploader_router
from api.health.health import router as health_router

app = FastAPI()

app.include_router(health_router)
app.include_router(resume_uploader_router)

