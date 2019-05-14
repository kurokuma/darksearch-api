# darksearch-api
https://darksearch.io/apidoc


```py
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from darksearch.darksearch import DarkSearch

ds = DarkSearch()

# ds.set_proxy("http", "160.16.69.219", 80)

# result = ds.search(query="dreammarket", page=9, data_type="raw_json")
# result = ds.search(query="dreammarket", page=1, data_type="json")
# result = ds.search(query="dreammarket", page=1, data_type="csv")
# print(result)

# result = ds.searches(query="dreammarket", data_type="raw_json", start_page=1, max_page=2)
# result = ds.searches(query="dreammarket", data_type="json", start_page=1, max_page=2)
# result = ds.searches(query="dreammarket", data_type="csv", start_page=1, max_page=2)

# print(result)

```

# requirements
- requests

```
> sudo pip3 install requests
```

# Demo

```
Data Response
- raw_json
{'last_page': last_page, 'total': total, 'per_page': per_page, 'to': to, 'data': [{'description': 'description', 'title': 'title', 'link': 'url'}, {'description': ...., 'from': from, 'current_page': current_page}

- json
[{'description': 'description', 'title': 'title', 'link': 'url'}, {'description': ....,]

- csv
[['description', 'title', 'url'], [.....]]

```
