from app.models.schemas import Classification

def decide(policy_id: str, cls: Classification):
    #T0: simple rules I can evolve later
    if cls.anonymity in ("tor", "proxy"):
        return "block", "ANON_BLOCK", "Tor/Proxy detected"
    if cls.connection_type == "hosting" and cls.confidence >= 80:
        return "allow", "DEFAULT_ALLOW", "No high risk signals"
    return "allow", "DEFAULT_ALLOW_ALL", "Allow Anything"