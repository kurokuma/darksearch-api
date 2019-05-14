# -*- coding: utf-8 -*-

from darksearch.darksearch import DarkSearch

ds = DarkSearch()

# ds.set_proxy("http", "160.16.69.219", 80)

# result = ds.search(query="dreammarket", page=9, data_type="raw_json")
# result = ds.search(query="dreammarket", page=1, data_type="json")
# result = ds.search(query="dreammarket", page=1, data_type="csv")
# print(result)

result = ds.searches(query="dreammarket", max_page=2)
print(result)
