# import module as m
# print("main name: ", __name__)
# m.hello()

# o = m.MyClass()

import requests
url = "http://127.0.0.1:5000"
# response = requests.get(f"{url}/posts/4/comments")

# print(response.status_code)
# print(response.text)

# response = requests.post(f"{url}/posts", 
#                          json={"title": "foo", 
#                                "body": "bar", "userId": 1})
response = requests.get(f"{url}/")
print(response.status_code, response.text)

response = requests.post(f"{url}/", json={"name": "foo"})
print(response.status_code, response.text)


response = requests.put(f"{url}/", json={"name": "bar"})
print(response.status_code, response.text)


response = requests.delete(f"{url}/")
print(response.status_code, response.text)

# j = response.json()
# print(type(j))
# print(j)
# # print(j["id"])

