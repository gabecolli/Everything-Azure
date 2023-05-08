import requests


body = {
  "Name": {
    "FirstName": "Gabriel",
    "LastName": "Colli"
    }
  }


response = requests.post("https://gabrielcolliapi.azurewebsites.net/api/HttpTrigger1", json=body)
print(response.text,response)