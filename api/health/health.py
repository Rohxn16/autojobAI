from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health():
    return {"status": "ok"}

@router.get("/health")
def health():
    return {"status": "ok"}