# darksearch-api
https://darksearch.io/apidoc


```py
# -*- coding: utf-8 -*-

from darksearch.darksearch import DarkSearch

ds = DarkSearch()

# ex
# get page 1
result = ds.search(query="dreammarket")
print(result)

# ex page=3
# get pages 1~3
result = ds.searchs(query="dreammarket", max_page=3)
print(result)
```

# requirements
- requests

```
> sudo pip3 install requests
```

# Demo

```
> python3 demo.py
{'last_page': 8, 'total': 143, 'per_page': 20, 'to': 20, 'data': [{'description': '#\n\n  * Start\n  * Bli medlem\n  * Logga in\n  * Till Flugsvamp (market)\n\nDu är inte inloggad.\n\n  * Start\n  * » DM, WallSt och andra marknader\n  * » ketamin på <em>dreammarket</em>\n\nSidor: 1\n\n## #1 2019-03-11 08:46:33\n\nmega\n\n    Medlem +\n    Registrerad: 2019-03-11\n    Inlägg: 123\n\n### ketamin på <em>dreammarket</em>', 'title': 'ketamin på dreammarket (sida 1) / DM, WallSt och andra marknader / Flugforum', 'link': 'http://flugforumt6eave4.onion/viewtopic.php?pid=6905#p6905'}, {'description': ...., 'from': 1, 'current_page': 1}
```
