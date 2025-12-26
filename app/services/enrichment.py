import ipaddress
from app.models.schemas import GeoInfo, NetworkInfo, Classification

def validate_ip(ip: str) -> str:
    ipaddress.ip_address(ip)
    return ip

def enrich_ip(ip: str):
    # T0: stub. Replace with real geo/asn/prefix + rdns caching later.
    geo = GeoInfo(country="US", region="TX", city="Dallas")
    network = NetworkInfo(asn=12345, org="Example Org", prefix="0.0.0.0/0")
    cls = Classification(
        connection_type="unknown",
        anonymity="unknown",
        confidence=10,
        risk_score=10,
        reasons=[{"code":"T0_STUB", "weight":1.0}],
        model_version="dev",
    )
    freshness = {"geo":"dev", "asn":"dev", "rdns":"live"}
    return geo, network, cls, freshness