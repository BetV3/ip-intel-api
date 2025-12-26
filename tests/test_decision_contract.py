import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_decision_contract():
    async with AsyncClient(base_url="http://test") as ac:
        r = await ac.post("/v1/decision", json={"ip":"8.8.8.8","policy_id":"signup-strict","context":{}})
        assert r.status_code == 200
        body = r.json()
        assert body["action"] in ("allow","challenge","block","review")
        assert "trace_id" in body