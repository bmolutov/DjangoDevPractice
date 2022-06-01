import requests 

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
        "title": "hey hey hey world",
        "price": 999.2
}

put_response = requests.put(endpoint, json=data)
print(put_response.json())
print(put_response.status_code)

