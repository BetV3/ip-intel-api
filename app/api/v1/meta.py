import os
from fastapi import APIRouter

router = APIRouter()

@router.get("/meta")
async def meta():
    return {
        "app": os.getenv("APP_NAME", "ip-intel-api"),
        "api_version": os.getenv("API_VERSION", "v1"),
        "build_sha": os.getenv("BUILD_SHA", "dev"),
        "data_version": os.getenv("DATA_VERSION", "dev"),
        "model_version": os.getenv("MODEL_VERSION", "dev"),
    }