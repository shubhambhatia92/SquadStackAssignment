
import requests
from requests.models import Response
API_TOKEN = "659c9fddb16335e48cc67114694b52074e812e03"
company_domain = "squadStack"
person_id = 13
URL="https://"+company_domain +"pipedrive.com/api//v1/persons/"+person_id+"/"+API_TOKEN

response = requests.get(url = URL)

if response.status_code == 200:
    print('person is present by this id')
    data=response.json
    print(data)
elif response.status_code == 404:
    print('Not Found.')


