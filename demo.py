# -*- coding: utf-8 -*-

from darksearch.darksearch import DarkSearch

ds = DarkSearch()

result = ds.search(query="dreammarket")
print(result)

# result = ds.searches(query="dreammarket", max_page=3)
# print(result)
