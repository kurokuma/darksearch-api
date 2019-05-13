# -*- coding: utf-8 -*-
import json
import requests

"""
API Documentation
https://darksearch.io/apidoc
"""

class DarkSearchException(Exception):
    def __init__(self, status_code, url, header):
        self.status_code = status_code
        self.url = url
        self.header = header
    
    def __repr__(self):
        return "status_code:{status_code} url:{url} header:{header}".format(
            status_code=self.status_code,
            url=self.url,
            header=self.header
        )
    __str__ = __repr__

class DarkSearchRateLimitException(DarkSearchException):
    pass
    """
    Afin d'éviter toute surcharge, notre API est limitée à 30 requêtes par minute.
    """

class DarkSearchAPIBase(object):
    BASE_URL = "https://darksearch.io/api/"
    BASE_HEADER = {
        "User-Agent": "DarkSearch Python API",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    EXCEPTION = {
        429: DarkSearchRateLimitException
    }
    PROXIES = None
    MAX_PAGE = 30
    PATH = None

    def __init__(self):
        pass
    
    def search(self, query, page=1):
        """
        query: search keyworkd(string)
        page: page number(int) default page 1
        """
        params = {
            "query": str(query),
            "page": int(page)
        }
        if self.PROXIES is None:
            r = requests.get(
                url=self.BASE_URL + self.PATH, 
                params=params, 
                headers=self.BASE_HEADER
            )
        else:
            r = requests.get(
                url=self.BASE_URL + self.PATH, 
                params=params, 
                headers=self.BASE_HEADER,
                proxies=self.PROXIES
            )

        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            try:
                return r.json()
            except Exception as e:
                print(e)
        else:
            ds_ex = self.EXCEPTION.get(r.status_code, DarkSearchException)
            raise ds_ex(
                status_code=r.status_code,
                url=r.url,
                header=r.headers
            )
    
    def searches(self, query, max_page=MAX_PAGE):
        """
        query: search keyword(string)
        max_page: 1~max_page(int) default max_page 30
        """
        res = []
        if max_page <= self.MAX_PAGE:
            for page in range(1, max_page+1):
                res.append(self.search(query=query, page=page))
            return res
        else:
            ds_ex = DarkSearchRateLimitException
            raise ds_ex(
                status_code="",
                url="",
                header=""
            )
    
    def set_proxy(self, proto, ip, port):
        """Set Proxy
        proto: ex)http or https..(string)
        ip: ipaddress or (string)
        port: port number(int or string)
        """
        self.PROXIES = {
            proto: "{proto}://{ip}:{port}".format(proto=proto, ip=ip, port=str(port))
        }