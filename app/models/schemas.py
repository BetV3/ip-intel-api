from pydantic import BaseModel, Field
from typing import Any, Dict, List, Literal, Optional

class NetworkInfo(BaseModel):
    asn: Optional[int] = None
    org: Optional[str] = None
    prefix: Optional[str] = None

class GeoInfo(BaseModel):
    country: Optional[str] = None
    region: Optional[str] = None
    city: Optional[str] = None

class Classification(BaseModel):
    connection_type: Optional[Literal["residential", "mobile", "hosting", "enterprise", "unknown"]] = "unknown"
    anonymity: Optional[Literal["none", "vpn", "tor", "unknown"]] = "unknown"
    confidence: int = Field(default=0, ge=0, le=100)
    risk_score: int = Field(default=0, ge=0, le=100)
    reasons: List[Dict[str, Any]] = Field(default_factory=list)
    model_version: str = "dev"
    
class IpLookupResponse(BaseModel):
    ip: str
    geo: GeoInfo
    network: NetworkInfo
    rdns: Optional[str] = None
    classifications: Classification
    freshness: Dict[str, str] = Field(default_factory=dict)
    trace_id: str

class DecisionRequest(BaseModel):
    ip: str
    policy_id: str = "signup-strict"
    context: Dict[str, Any] = Field(default_factory=dict)
    
class DecisionResponse(BaseModel):
    action: Literal["allow", "challenge", "block", "review"]
    reason: str
    rule_id: str
    trace_id: str