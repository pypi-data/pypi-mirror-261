import enum
from typing import Dict, List, Optional
from aiohttp import ClientSession, ContentTypeError

from async_cloudflare.models import ScanDNS, DNSRecord, CreateDNSRecord, DNSDelete, Zone, ZoneCreate


class RequestMethods(enum.StrEnum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class RequestAiohttp:
    __BASE_URL = "https://api.cloudflare.com/client/v4"

    def __init__(self, session, headers):
        self.__session = session
        self.__headers = headers

    async def _request(self, method: RequestMethods, url: str, **args) -> dict | List[dict]:
        response = await self.__session.request(method, self.__BASE_URL + url, headers=self.__headers, **args)
        try:
            jsoned: dict = await response.json()
        except ContentTypeError:
            raise Exception(await response.text())
        if not jsoned.get("success"):
            errors = jsoned.get("errors") or jsoned.get("error")
            raise Exception(errors)
        return jsoned.get("result")


class CloudFlare:
    def __init__(self, token: str, email: str, auth_key: str, account_id: Optional[str] = None) -> None:
        if token and not isinstance(token, str):
            raise TypeError(f"Token {token} must be string")
        self.__headers = {"Content-Type": "application/json",
                          "Authorization": f"Bearer {token}",
                          "X-Auth-Email": email,
                          "X-Auth-Key": auth_key}
        self.__session = ClientSession()
        self.__token: str = token
        self.__account_id = account_id
        self.zones: ZonesAPI = ZonesAPI(self.__session, self.__headers, self.__account_id)
        self.accounts: AccountsAPI = AccountsAPI(self.__session, self.__headers, self.__account_id)


class AccountsAPI(RequestAiohttp):
    def __init__(self, session: ClientSession, headers: Dict[str, str], account_id: Optional[str] = None) -> None:
        super().__init__(session, headers)
        self.__account_id = account_id

    async def getCustomNameservers(self):
        if not self.__account_id:
            raise Exception("account_id not set")
        response: List[dict] = await self._request(RequestMethods.GET, f"/accounts/{self.__account_id}/custom_ns")
        print(response)

    async def get(self):
        if not self.__account_id:
            raise Exception("account_id not set")
        response: List[dict] = await self._request(RequestMethods.GET, f"/accounts/{self.__account_id}")
        print(response)


class ZonesAPI(RequestAiohttp):
    def __init__(self, session: ClientSession, headers: Dict[str, str], account_id: Optional[str] = None) -> None:
        super().__init__(session, headers)
        self.dns_records: DNSRecords = DNSRecords(session, headers)
        self.__account_id = account_id

    async def get(self, account_id: Optional[str] = None, name: Optional[str] = None) -> List[Zone]:
        params = {}
        if account_id:
            params["account.id"] = account_id
        if name:
            params["name"] = name

        response: List[dict] = await self._request(RequestMethods.GET, "/zones", params=params)
        return [Zone(**zone_dict) for zone_dict in response]

    async def create(self, zone_data: ZoneCreate) -> Zone:
        if not self.__account_id:
            raise Exception("account_id not set")
        data = zone_data.model_dump()
        data["account"] = {"id": self.__account_id}
        response: dict = await self._request(RequestMethods.POST, "/zones", json=data)
        return Zone(**response)


class DNSRecords(RequestAiohttp):

    # todo: add dns export
    # todo: add dns import
    # todo: add dns details
    # todo: add dns overwrite
    def __init__(self, session: ClientSession, headers: Dict[str, str]) -> None:
        super().__init__(session, headers)

    async def scan(self, zone_id: str) -> ScanDNS:
        response: dict = await self._request(RequestMethods.POST, f"/zones/{zone_id}/dns_records/scan")
        return ScanDNS(**response)

    async def create(self, zone_id: str, dns_record: CreateDNSRecord) -> DNSRecord:
        data = dns_record.model_dump(exclude_none=True)
        response: dict = await self._request(RequestMethods.POST, f"/zones/{zone_id}/dns_records", json=data)
        return DNSRecord(**response)

    async def delete(self, zone_id: str, dns_record_id: str) -> DNSDelete:
        response: dict = await self._request(RequestMethods.DELETE, f"/zones/{zone_id}/dns_records/{dns_record_id}")
        return DNSDelete(**response)

    async def update(self, zone_id: str, dns_record_id: str, dns_record: CreateDNSRecord) -> DNSRecord:
        data = dns_record.model_dump(exclude_none=True)
        response: dict = await self._request(RequestMethods.PATCH, f"/zones/{zone_id}/dns_records/{dns_record_id}",
                                             json=data)
        return DNSRecord(**response)

    async def __call__(self, zone_id: str) -> List[DNSRecord]:
        response: List[dict] = await self._request(RequestMethods.GET, f"/zones/{zone_id}/dns_records")
        return [DNSRecord(**dns_record) for dns_record in response]
