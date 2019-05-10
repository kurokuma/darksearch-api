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
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    EXCEPTION = {
        429: DarkSearchRateLimitException
    }

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
        r = requests.get(url=self.BASE_URL + self.PATH, params=params, headers=self.BASE_HEADER)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            try:
                return r.json()
            except UnicodeEncodeError as e:
                print(e)
        else:
            ds_ex = self.EXCEPTION.get(r.status_code, DarkSearchException)
            raise ds_ex(
                status_code=r.status_code,
                url=r.url,
                header=r.headers
            )
    
    def searchs(self, query, max_page=MAX_PAGE):
        """
        query: search keyword(string)
        max_page: 1~max_page(int) default max_page 30
        """
        res = []
        for page in range(1, max_page+1):
            res.append(self.search(query=query, page=page))
        return res