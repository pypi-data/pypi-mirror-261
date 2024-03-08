"""
Loqed API integration
"""

import logging
import aiohttp
#from .apiclient import APIClient
from typing import List
import os
import json
from abc import abstractmethod
from asyncio import CancelledError, TimeoutError, get_event_loop
from aiohttp import ClientError, ClientSession, ClientResponse
from typing import List

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger("trace")

class AbstractAPIClient():
    """Client to handle API calls."""

    def __init__(self, websession: ClientSession, host):
        """Initialize the client."""
        self.websession = websession
        self.host = host
        print("API CLIENT CREATED")

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def request(self, method, url, **kwargs) -> ClientResponse:
        """Make a request."""
        headers = kwargs.get("headers")

        if headers is None:
            headers = {}
        else:
            headers = dict(headers)

        access_token = await self.async_get_access_token()
        headers["authorization"] = f"Bearer {access_token}"

        return await self.websession.request(
            method, f"{self.host}/{url}", **kwargs, headers=headers,
        )


class APIClient(AbstractAPIClient):
    def __init__(self, websession: ClientSession, host: str, token: str):
        """Initialize the auth."""
        super().__init__(websession, host)
        self.token = token

    async def async_get_access_token(self) -> str:
        """Return a valid access token."""
        return self.token
        


class Lock:
    """Class that represents a Lock object in the LoqedAPI."""

    def __init__(self, raw_data: dict, apiclient: APIClient):
        """Initialize a lock object."""
        self.raw_data = raw_data
        self.apiclient = apiclient
        self.webhooks = {}
        self.bolt_state=self.raw_data["bolt_state"]
    

    @property
    def id(self) -> str:
        """Return the ID of the lock."""
        return self.raw_data["id"]

    @property
    def name(self) -> str:
        """Return the name of the lock."""
        return self.raw_data["name"]
    
    @property
    def battery_percentage(self) -> int:
        """Return the name of the lock."""
        return self.raw_data["battery_percentage"]

    @property
    def battery_type(self) -> str:
        """Return the name of the lock."""
        return self.raw_data["battery_type"]

    # @property
    # def bolt_state(self) -> str:
    #     """Return the state of the lock."""
    #     return self.bolt_state

    @property
    def party_mode(self) -> bool:
        """Return the name of the lock."""
        return self.raw_data["party_mode"]

    @property
    def guest_access_mode(self) -> bool:
        """Return the name of the lock."""
        return self.raw_data["guest_access_mode"]

    @property
    def twist_assist(self) -> bool:
        """Return the name of the lock."""
        return self.raw_data["twist_assist"]

    @property
    def touch_to_connect(self) -> bool:
        """Return the name of the lock."""
        return self.raw_data["touch_to_connect"]
    
    @property
    def lock_direction(self) -> str:
        """Return the name of the lock."""
        return self.raw_data["lock_direction"]
    
    @property
    def mortise_lock_type(self) -> str:
        """Return the name of the lock."""
        return self.raw_data["mortise_lock_type"]

    @property
    def supported_lock_states(self) -> str:
        """Return the name of the lock."""
        return self.raw_data["supported_lock_states"]

    async def open(self):
        "Open the lock"
        resp = await self.apiclient.request("get", f"locks/{self.id}/bolt_state/open")
        resp.raise_for_status()
        print("Response" + await resp.text())

    async def lock(self):
        "Set night-lock"
        resp = await self.apiclient.request("get", f"locks/{self.id}/bolt_state/night_lock")
        resp.raise_for_status()
        print("Response" + await resp.text())
    
    async def unlock(self):
        "Set day-lock"
        resp = await self.apiclient.request("get", f"locks/{self.id}/bolt_state/day_lock")
        resp.raise_for_status()
        print("Response" + await resp.text())
    
    async def update(self):
        "Update status"
        resp = await self.apiclient.request("get", "locks")
        resp.raise_for_status()
        json_data = await resp.json()
        for lock_data in json_data["data"]:
            if lock_data["id"]==self.raw_data["id"]:
                self.raw_data=lock_data
                self.bolt_state=self.raw_data["bolt_state"]
        print("Response UPDATED" + await resp.text())

    async def getWebhooks(self):
        "Get webhooks for this lock"
        resp = await self.apiclient.request("get", f"locks/{self.id}/webhooks")
        resp.raise_for_status()
        json_data = await resp.json()
        print("Response" + str(json_data))
        for hook in json_data["data"]:
            print("FOUND WEBHOOK:" + str(hook))
        self.webhooks=json_data["data"]
        return json_data["data"]

    async def registerWebhook(self, url):
        "Register webhook for this lock"
        resp = await self.apiclient.request("post", f"locks/{self.id}/webhooks", json={"url": url})
        resp.raise_for_status()
        await self.getWebhooks()
        print("Response" + await resp.text())

    async def updateState(self, state):
        self.bolt_state=state



class LoqedAPI:

    def __init__(self, apiclient: APIClient):
        """Initialize the API and store the auth so we can make requests."""
        self.apiclient = apiclient

    async def async_get_locks(self) -> List[Lock]:
        """Return the locks."""
        resp = await self.apiclient.request("get", "locks")
        print("Response" + await resp.text())
        json_data = await resp.json()
        return [Lock(lock_data, self.apiclient) for lock_data in json_data["data"]]


# NOT supported in API Yet
    # async def async_get_lock(self, lock_id) -> Lock:
    #     """Return a Lock."""
    #     resp = await self.apiclient.request("get", f"lock/{lock_id}")
    #     resp.raise_for_status()
    #     return Lock(await resp.json(), self.apiclient)



   
"""Loqed: Exceptions"""


class LoqedException(BaseException):
    """Raise this when something is off."""


class LoqedAuthenticationException(LoqedException):
    """Raise this when there is an authentication issue."""


