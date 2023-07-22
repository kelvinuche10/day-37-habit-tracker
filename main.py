import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = your_username
TOKEN = your_self_created_token
GRAPH_ID = your_graph_id

user_params = {
	'token': TOKEN,
	'username': USERNAME,
	'agreeTermsOfService': 'yes',
	'notMinor': 'yes',
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

headers = {
	'X-USER-TOKEN': TOKEN
}

user_params = {
	'id': GRAPH_ID,
	'name': 'Thinking Habit Tracker',
	'unit': 'hour',
	'type': 'int',
	'color': 'sora',

}

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_params = {
	'date': today.strftime('%Y%m%d'),
	'quantity': '4', 
}
response = requests.post(url=post_pixel_endpoint, headers=headers, json=pixel_params)
print(response.text)
