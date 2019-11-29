'''
json response from yahoo api (url)
'''
# TODO: Find a simple url to return currency conversion response in json.
#       Preferably yahoo.

import json
from urllib.request import urlopen

# WARNING: Discontinued.
URL = (
"https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"
)

with urlopen(URL) as response:
    source = response.read()


print(source)