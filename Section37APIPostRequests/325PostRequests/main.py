import requests
from decouple import config
import datetime

pixela_token = config("pixela_token")

pixela_endpoint = "https://pixe.la/v1/users"
pixela_username = "paulvatterott"
graph_id = "graph1"

# user_params = {
#     "token": pixela_token,
#     "username": "paulvatterott",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

# graph_params = {
#     "id": "graph1",
#     "name": "Working Out Graph",
#     "unit": "minutes",
#     "type": "float",
#     "color": "ajisai"
# }

# headers = {
#     "X-USER-TOKEN": pixela_token
# }

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}"
today = datetime.date.today()
formatted_date = today.strftime('%Y%m%d')


pixel_params = {
    "date": formatted_date,
    "quantity": "50.00"

}

headers = {
    "X-USER-TOKEN": pixela_token
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
