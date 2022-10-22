import requests
import config

#Create the user

pixela_ep = "https://pixe.la/v1/users"
graph_ep = f'{pixela_ep}/{config.username}/graphs'

user_params={
    'token': config.token,
    'username': config.username,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}


# r_user=requests.post(url=pixela_ep, json=user_params)
# print(r_user.text)

#Create the graph

graph_params = {
    "id" : "graph1",
    "name" : "Coding timer graph",
    "unit" : "minutes",
    "type" : "float",
    "color" : "shibafu",
}

headers={
    'X-USER-TOKEN': config.token,
    }
#r_graph=requests.post(url=graph_ep,json=graph_params ,headers=headers)
#print(r_graph.text)

#Create a pixel

pixel_ep = f'{pixela_ep}/{config.username}/graphs/graph1'

pixel_params={
    'date':'20221022',
    'quantity':"60.0",
}

r_pixel= requests.post(url=pixel_ep, json=pixel_params, headers=headers)
print(r_pixel.text)

