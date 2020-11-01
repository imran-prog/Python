import requests



'''
response = requests.get("https://google.com")
# print(response.content)
# print(response.text)
# print(response.json())
print(response.headers)
'''

'''
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except Exception as err:
        print(f"Other error occured: {err}")
    else:
        print("Success")
'''

'''
# Simple Commands for Request Module
print(req)
print(req.status_code)

# using Conditions to make it more user friendly
if req.status_code == 200:
    print("Success")
else:
    print("Not found")
'''
