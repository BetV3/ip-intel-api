from fastapi import APIRouter

router = APIRouter()

@router.get("/healthz")
async def healthz():
    return {"ok": True}

@router.get("/readyz")
async def readyz():
    # verify datasets, db reachable, etc. Later implementation
    return {"ready": True}