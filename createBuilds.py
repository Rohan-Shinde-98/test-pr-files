import requests
import os
import json

def triggerBuilds(fileName):
  body={
    "request": {
      "config": {
          "script": fileName,
          "arch": "s390x"
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

 
file = open('changed_files.txt','r')
for data in file:
  print(data[0])
