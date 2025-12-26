from fastapi import APIRouter, Request, HTTPException
from app.models.schemas import IpLookupResponse
from app.services.enrichment import validate_ip, enrich_ip

router = APIRouter()

@router.get('/ip/{ip}', response_model=IpLookupResponse)
async def ip_lookup(ip: str, request: Request):
    try:
        validate_ip(ip)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid IP Address")
    geo, network, cls, freshness = enrich_ip(ip)
    return IpLookupResponse(
        ip=ip,
        geo=geo,
        network=network, 
        rdns=None,
        classifications=cls,
        freshness=freshness,
        trace_id=request.state.trace_id,
    )