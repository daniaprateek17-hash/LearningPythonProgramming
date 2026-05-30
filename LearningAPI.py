import requests

url = "https://dummyjson.com/users"  

respone = requests.get(url)

data = respone.json()
print(data)
