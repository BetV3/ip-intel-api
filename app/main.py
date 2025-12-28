from fastapi import FastAPI

from app.core.middleware import TraceIdMiddleware
from app.api.v1.router import router


app = FastAPI(title="ip-intel-api")

app.add_middleware(TraceIdMiddleware)
app.include_router(router, prefix="/v1")