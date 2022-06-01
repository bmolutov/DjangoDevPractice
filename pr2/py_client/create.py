import requests 

endpoint = "http://localhost:8000/api/products/"

data = {
        "title": "this field is done"
}

post_response = requests.post(endpoint, json=data)

print(post_response.content)
print(post_response.status_code)

