import requests
import os

def triggerBuilds(file):
  body={
    "request": {
    "message": "Override the commit message: this is an api request",
    "branch":"master",
    "merge_mode": "replace",
    "config": {
        "env": {
          "jobs": [
            "TEST=unit"
          ]
        },
        "script": "echo 'hello world'"
      }
    }}
  
  headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Travis-API-Version": "3",
    "Authorization": "token " +  os.environ['AUTH_TOKEN']
  }
  
  response = requests.post("https://api.travis-ci.com/repo/Rohan-Shinde-98%2Ftest-pr-files/requests", data=body, headers=headers)
  print(response.text)
  
  
triggerBuilds("echo 'Hello World'")
