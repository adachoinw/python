import requests
from datetime import datetime

USERNAME = "katyperrytiger"
TOKEN = "thisissecret"

# create a user
pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)
# successfully created a user:
# {"message":"Success. Let's visit https://pixe.la/@katyperrytiger , it is your profile page!","isSuccess":true}

###############################################################################################
#create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# graph created: https://pixe.la/v1/users/katyperrytiger/graphs/graph1.html
###############################################################################################

# post a pixel:
pixel_endpoint = f"{graph_endpoint}/graph1"

# today = datetime.now()
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
# https://pixe.la/v1/users/katyperrytiger/graphs/graph1.html

###############################################################################################
#update a pixel
pixel_update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
pixel_update_config = {
    "quantity": "16.8"
}

# response = requests.put(pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)
#https://pixe.la/v1/users/katyperrytiger/graphs/graph1.html


###############################################################################################
#delete a pixel
pixel_delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
