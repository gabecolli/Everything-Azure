import requests


body = {
  "Name": {
    "FirstName": "Gabriel",
    "LastName": "myname"
    }
  }


response = requests.post("your function app here", json=body)
print(response.text,response)