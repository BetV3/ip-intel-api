import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_ip_lookup_contract():
    async with AsyncClient(base_url="http://test") as ac:
        r = await ac.get("/v1/ip/8.8.8.8")
        assert r.status_code == 200
        body = r.json()
        assert "trace_id" in body
        assert body["ip"] == "8.8.8.8"
        assert "network" in body and "geo" in body and "classifications" in body