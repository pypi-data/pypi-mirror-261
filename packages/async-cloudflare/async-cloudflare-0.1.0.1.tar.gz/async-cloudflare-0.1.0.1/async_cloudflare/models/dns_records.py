from datetime import datetime
from typing import Optional, List, Literal

from pydantic import BaseModel


class CreateDNSRecord(BaseModel):
    content: str
    name: str
    type: Literal["A"] = "A"
    proxied: Optional[bool] = True
    comment: Optional[str] = None
    tags: Optional[List[str]] = None
    ttl: Optional[int] = 1


class ScanDNS(BaseModel):
    recs_added: int
    recs_added_by_type: dict
    total_records_parsed: int


class DNSRecord(BaseModel):
    id: str
    zone_id: str
    zone_name: str
    name: str
    type: str
    content: str
    proxiable: bool
    proxied: bool
    ttl: int
    locked: bool
    meta: "Meta"
    comment: Optional[str] = None
    tags: List[str]
    created_on: datetime
    modified_on: datetime

    class Meta(BaseModel):
        auto_added: bool
        managed_by_apps: bool
        managed_by_argo_tunnel: bool


class DNSDelete(BaseModel):
    id: str
