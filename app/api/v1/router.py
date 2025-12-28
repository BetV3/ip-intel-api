from fastapi import APIRouter
from app.api.v1.ip_lookup import router as ip_router
from app.api.v1.decision import router as decision_router
from app.api.v1.health import router as health_router
from app.api.v1.meta import router as meta_router

router = APIRouter()
router.include_router(ip_router, tags=["ip"])
router.include_router(decision_router, tags=["decision"])
router.include_router(health_router, tags=["health"])
router.include_router(meta_router, tags=["meta"])