# -*- coding: utf-8 -*-

from darksearch.darksearch import DarkSearch

ds = DarkSearch()

# ds.set_proxy("http", "160.16.69.219", 80)

result = ds.search(query="dreammarket")
print(result)

# result = ds.searches(query="dreammarket", max_page=31)
# print(result)
