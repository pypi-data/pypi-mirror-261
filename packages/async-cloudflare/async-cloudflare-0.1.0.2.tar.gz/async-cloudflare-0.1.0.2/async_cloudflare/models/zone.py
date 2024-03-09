from typing import List, Optional, Literal

from pydantic import BaseModel
from datetime import datetime


class Account(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class Zone(BaseModel):
    account: Account
    activated_on: Optional[datetime] = None
    created_on: datetime
    development_mode: int
    id: str
    modified_on: datetime
    name: str
    original_dnshost: Optional[str] = None
    original_name_servers: Optional[List[str]] = None
    original_registrar: Optional[str] = None
    owner: Account
    vanity_name_servers: Optional[List[str]] = None
    name_servers: Optional[List[str]] = []


class ZoneCreate(BaseModel):
    name: str
    type: Literal["full", "partial", "secondary"] = "full"
