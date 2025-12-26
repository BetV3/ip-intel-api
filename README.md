# ip-intel-api (T0)

## Run
1. Copy env:
   cp .env.example .env

2. Start:
   docker compose up --build

## Test
pytest -q

## Try it
curl http://localhost:8000/v1/ip/8.8.8.8
curl -X POST http://localhost:8000/v1/decision \
  -H "Content-Type: application/json" \
  -d '{"ip":"8.8.8.8","policy_id":"signup-strict","context":{"new_user":true}}'