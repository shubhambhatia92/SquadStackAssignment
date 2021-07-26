
import requests
from requests.models import Response
API_TOKEN = "659c9fddb16335e48cc67114694b52074e812e03"
company_domain = "squadStack"
person_id = 13;
URL="https://"+company_domain +"pipedrive.com/api/v1/persons/"+person_id+"/"+API_TOKEN



# data to be sent to api
data = {'Name':'shubham bhatia',
		'phone':'7007793844',
		'owner_id':'1234',
	}

response = requests.put(url = URL, data = data)


if response.status_code == 200:
    print('person is updates')
elif response.status_code == 404:
    print('Not Found.')
