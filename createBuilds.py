import requests
import os
import json

def triggerBuilds(file):
  body={
    "request": {
      "config": {
          "script": "echo 'hello world'"
        }
      }
  }
  
  headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Travis-API-Version": "3",
    "Authorization": "token " +  os.environ['AUTH_TOKEN']
  }
  
  response = requests.post("https://api.travis-ci.com/repo/Rohan-Shinde-98%2Ftest-trigger-build/requests", data=json.dumps(body), headers=headers)
  print(response.text)
  
  
triggerBuilds("echo 'Hello World'")
