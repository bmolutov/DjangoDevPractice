import requests 

endpoint = "http://localhost:8000/api/products/"

data = {
        "title": "this field is done"
}

get_response = requests.get(endpoint)

print(get_response.content)
print(get_response.status_code)

