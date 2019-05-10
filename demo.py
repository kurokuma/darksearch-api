# -*- coding: utf-8 -*-

from darksearch.darksearch import DarkSearch

ds = DarkSearch()

result = ds.search(query="dreammarket")
print(result)

# result = ds.searchs(query="dreammarket", max_page=3)
# print(result)
