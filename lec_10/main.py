# import module as m
# print("main name: ", __name__)
# m.hello()

# o = m.MyClass()

import requests
url = "https://jsonplaceholder.typicode.com"
# response = requests.get(f"{url}/posts/4/comments")

# print(response.status_code)
# print(response.text)

response = requests.post(f"{url}/posts", 
                         json={"title": "foo", 
                               "body": "bar", "userId": 1})
print(response.status_code)
print(response.text)

j = response.json()
print(type(j))
print(j["id"])
