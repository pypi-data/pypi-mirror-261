
#    If you have anything bad to say about this file, put it up your ass because I know what to do


import httpx
import json
from typing import Union
from hmac import new
from hashlib import sha1
from base64 import b64encode
from os import urandom
from time import time as timestamp


# by Xsarz
class Generator:
    PREFIX = bytes.fromhex("19")
    SIG_KEY = bytes.fromhex("DFA5ED192DDA6E88A12FE12130DC6206B1251E44")
    DEVICE_KEY = bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9")

    @staticmethod
    def signature(data: Union[str, bytes]) -> str:
        data = data if isinstance(data, bytes) else data.encode("utf-8")
        return b64encode(Generator.PREFIX + new(Generator.SIG_KEY, data, sha1).digest()).decode("utf-8")

    @staticmethod
    def generate_device_id():
        ur = Generator.PREFIX + (urandom(20))
        mac = new(Generator.DEVICE_KEY, ur, sha1)
        return f"{ur.hex()}{mac.hexdigest()}".upper()


class Headers:
    def __init__(self, data=None, content_type=None, sid: str = None):
        self.device = Generator.generate_device_id()
        self.user_agent = "Apple iPhone12,1 iOS v15.5 Main/3.12.2"
        self.sid = sid
        self.headers = {
            "NDCDEVICEID": self.device,
            "NDCLANG": "en",
            "Accept-Language": "en-US",
            "User-Agent": self.user_agent,
            "Content-Type": "application/json; charset=utf-8",
            "Host": "service.aminoapps.com",
            "Accept-Encoding": "gzip",
            "Connection": "Upgrade"
        }
        if data:
            self.headers["Content-Length"] = str(len(data))
            self.headers["NDC-MSG-SIG"] = Generator.signature(data=data)
        if self.sid:
            self.headers["NDCAUTH"] = f"sid={self.sid}"
        if content_type:
            self.headers["Content-Type"] = content_type



class Client:
    def __init__(self,proxies: dict = None):
      self.device_id = Generator.generate_device_id()
      self.proxies = proxies
      self.comId = None


    def request(self, method, endpoint, headers=None, data=None):
        url = f"https://service.aminoapps.com/api/v1/{endpoint}"
        if method == "POST":
            response = httpx.post(url, headers=headers, data=data,proxies=self.proxies)
        elif method == "GET":
            response = httpx.get(url, headers=headers,proxies=self.proxies)
        elif method == "DELETE":
            response = httpx.delete(url, headers=headers,proxies=self.proxies)
        else:
            return "Method not found"

        return response

# Account
    def login(self, email: str, password: str , clientType: int = 100):
      data = json.dumps({
      "email": email,
            "v": 2,
            "secret": f"0 {password}",
            "deviceID": self.device_id,
            "clientType": clientType,
            "action": "normal",
            "timestamp": int(timestamp() * 1000)
        })
      response = self.request(method="POST", endpoint="g/s/auth/login", headers=Headers(data=data, content_type="application/json").headers, data=data).json()
      try:
        self.sid = response["sid"]
      except:pass
      return response

    def get_from_link(self, link: str):
      return self.request(method="GET", endpoint=f"g/s/link-resolution?q={link}", headers=Headers().headers).json()["linkInfoV2"]["extensions"]["linkInfo"]

    def set_comId(self,comId: str):
      self.comId = comId
      return self



# community
    def join_community(self):
        data = {"timestamp": int(timestamp() * 1000)}
        data = json.dumps(data)
        response = self.request(method="POST", endpoint=f"x{self.comId}/s/community/join", data=data, headers=Headers(data=data).headers).json()
        return response

    def edit_chat(self, chatId: str, announcement: str):
      data=json.dumps({"extensions": {"announcement": announcement,"pinAnnouncement": True},"timestamp": int(timestamp() * 1000)})
      response=self.request(method="POST", endpoint=f"x{self.comId}/s/chat/thread/{chatId}", headers=Headers(data=data).headers, data=data).json()
      return response

