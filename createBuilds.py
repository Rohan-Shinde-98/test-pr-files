import requests
import os
import json

def triggerBuilds(file):
  body={
    "request": {
    "message": "Override the commit message: this is an api request",
    "branch":"master",
#     "merge_mode": "replace",
    "config": {
        "env": {
          "jobs": [
            "TEST=unit"
          ]
        },
        "script": "echo 'hello world'",
        "merge_mode": "replace",
      }
    }}
  
  headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Travis-API-Version": "3",
    "Authorization": "token " +  os.environ['AUTH_TOKEN']
  }
  
  response = requests.post("https://api.travis-ci.com/repo/Rohan-Shinde-98%2Ftest-trigger-build/requests", data=json.dumps(body), headers=headers)
  print(response.text)
  
  
triggerBuilds("echo 'Hello World'")
