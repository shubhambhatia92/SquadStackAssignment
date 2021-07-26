import requests
from requests.models import Response
API_TOKEN = "659c9fddb16335e48cc67114694b52074e812e03"
company_domain = "squadStack"
URL="https://"+company_domain +"pipedrive.com/api/v1/persons/search"+API_TOKEN
name  = "shubham"
terms='example'
PARAMS = {'field':name,'terms':terms}

response = requests.get(url = URL, params = PARAMS)

if response.status_code == 200:
    print('Success!')
    data=response.json
    print(data)
elif response.status_code == 404:
    print('Not Found.')


