from fastapi import FastAPI, HTTPException
from api.resume_uploader.resume_upload import  router as resume_uploader_router
from api.health.health import router as health_router
from api.job_query.query import router as job_query_router

app = FastAPI()

app.include_router(health_router)
app.include_router(resume_uploader_router)
app.include_router(job_query_router)
    
