import requests
from requests.models import Response
API_TOKEN = "659c9fddb16335e48cc67114694b52074e812e03"
company_domain = "squadStack"
person_id = 13
URL="https://"+company_domain +"pipedrive.com/api/v1/notes/"+"/"+API_TOKEN


data = {'content':'please hire me squad stack is a great company ',
		'person_id':person_id
	}

response = requests.post(url = URL, data = data)

if response.status_code == 200:
    print('note has been added to given person id')
elif response.status_code == 404:
    print('failed')

