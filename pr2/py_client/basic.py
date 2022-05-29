import requests 

endpoint = "http://localhost:8000/api/"


post_response = requests.post(endpoint, json={"title": "hello world"})
print(post_response.content)
print(post_response.status_code)


# get_response = requests.get(endpoint)
# print(get_response.content)
# print(get_response.status_code)

