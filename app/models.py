from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

class ServiceCreate(BaseModel):
    name: str = Field(min_length=2, max_length=64)
    url: HttpUrl
    enabled: bool = True

class ServiceOut(BaseModel):
    service_id: str
    name: str
    url: str
    enabled: bool
    created_at: str

class StatusOut(BaseModel):
    service_id: str
    checked_at: str
    status: str
    latency_ms: Optional[int] = None
    http_code: Optional[int] = None
    error: Optional[str] = None