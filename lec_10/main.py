# import module as m
# print("main name: ", __name__)
# m.hello()

# o = m.MyClass()

import requests

response = requests.get('https://www.google.com')

print(response.status_code)
print(response.text)