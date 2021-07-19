import requests
import os
import json
import glob

def triggerBuilds(fileName):
  body={
    "request": {
      "config": {
          "script": fileName
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
  

all_files = glob.glob('./*.sh')
print(all_files)
triggerBuilds(all_files[0])
