from fastapi import FastAPI

from app.core.middleware import TraceIdMiddleware


app = FastAPI(title="ip-intel-api")

app.add_middleware(TraceIdMiddleware)