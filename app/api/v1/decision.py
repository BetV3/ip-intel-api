from fastapi import APIRouter, Request, HTTPException
from app.models.schemas import DecisionRequest, DecisionResponse
from app.services.enrichment import validate_ip, enrich_ip
from app.services.decision_engine import decide

router = APIRouter()

@router.post("/decision", response_model=DecisionResponse)
async def decision(req: DecisionRequest, request: Request):
    try:
        validate_ip(req.ip)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid IP Address")
    _, _, cls, _ = enrich_ip(req.ip)
    action, rule_id, reason = decide(req.policy_id, cls)
    return DecisionResponse(action=action, rule_id=rule_id, reason=reason, trace_id=request.state.trace_id)