import requests
"""
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response)
print(response.text)
print(response.json())

params = {
    "name" : "Romaan",
    "age" :22,
    "city":"Lahore"
}
response= requests.get("https://jsonplaceholder.typicode.com/posts/1",params=params)
print(response.status_code)

print("\nData of params by JSON:\n",response.json())
print("\nData of params by TEXT:\n",response.json())

headers = {
    "Authorization": "Bearer TOKEN",
    "Content-Type": "application/json"
}

response= requests.get("https://httpbin.org/get")
print(response.status_code)
#print("\nData of same key with different values of params by JSON:",response.hearders())

"""
data ={
    "name":"Romaan",
    "age":22,
    "skill":"Backend developer"
}
response=requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
print(response.status_code)
print(response.text)

response = requests.post("https://jsonplaceholder.typicode.com/posts",json={"name":"Hassan","age":23,"skill":"frontend developer"})
print(response.json())


