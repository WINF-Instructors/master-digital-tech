import requests

url = "https://www.google.com"
response=requests.get(url)
if response.status_code not in [200, 201, 202]:
    print("Schief gegangen")
else:
    print(response.text)