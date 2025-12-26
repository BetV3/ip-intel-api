import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

TRACE_HEADER = "x-trace-id"

class TraceIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        trace_id = request.headers.get(TRACE_HEADER) or str(uuid.uuid4())
        request.state.trace_id = trace_id
        response: Response = await call_next(request)
        response.headers[TRACE_HEADER] = trace_id
        return response