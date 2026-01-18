from fastapi import FastAPI, HTTPException
from datetime import datetime,timezone
import os, uuid
import httpx

from models import ServiceCreate,ServiceOut, StatusOut
import db

app = FastAPI(title = "aws-cicd-eks-ecr-alb", version="1.0.0")

REQUEST_TIMEOUT = float(os.getenv("CHECK_TIMEOUT_SECONDS","3.0"))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/services", response_model=ServiceOut)
def create_service(payload: ServiceCreate):
    service_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()

    item = {
        "service_id": service_id,
        "name": payload.name,
        "url": str(payload.url),
        "enabled": payload.enabled,
        "created_at": now,
    }
    db.put_service(item)
    return item

@app.get("/services", response_model=list[ServiceOut])
def get_services():
    return db.list_services()

@app.get("/status", response_model=list[StatusOut])
async def run_checks():
    services = [s for s in db.list_services() if s.get("enabled", True)]
    now = datetime.now(timezone.utc).isoformat()

    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT, follow_redirects=True) as client:
        results = []
        for s in services:
            service_id = s["service_id"]
            url = s["url"]
            checked_at = now

            try:
                start = datetime.now(timezone.utc)
                r = await client.get(url)
                end = datetime.now(timezone.utc)
                latency_ms = int((end - start).total_seconds() * 1000)

                status = "UP" if 200 <= r.status_code < 400 else "DOWN"

                item = {
                    "service_id": service_id,
                    "checked_at": checked_at,
                    "status": status,
                    "latency_ms": latency_ms,
                    "http_code": r.status_code,
                    "error": None,
                }
            except Exception as e:
                item = {
                    "service_id": service_id,
                    "checked_at": checked_at,
                    "status": "DOWN",
                    "latency_ms": None,
                    "http_code": None,
                    "error": str(e),
                }
            
            db.put_status(item)
            results.append(item)
            
    return results
    
@app.get("/status/{service_id}/latest", response_model=StatusOut)
def latest(service_id: str):
    item = db.get_latest_status(service_id)
    if not item:
        raise HTTPException(status_code=404, detail = "No status found")
    return item

@app.get("/status/{service_id}/history", response_model=list[StatusOut])
def history(service_id: str, limit: int = 20):
    return db.list_status_history(service_id, limit=limit)

