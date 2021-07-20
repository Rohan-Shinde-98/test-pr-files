import requests
import os
import json

def triggerBuilds(fileName, fileURL):
  body={
    "request": {
      "config": {
          "script": [ "wget " + fileURL, "bash " + fileName ],
          "arch": "ppc64le",
          "merge_mode": "replace"
        }
      }
  }
  
  headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Travis-API-Version": "3",
    "Authorization": "token " +  os.environ['AUTH_TOKEN']
  }
  
  response = requests.post("https://api.travis-ci.com/repo/Rohan-Shinde-98%2Ftest-pr-files/requests", data=json.dumps(body), headers=headers)

 
files = open('changed_files.txt','r')
for file in files:
  content = file.split()
  triggerBuilds(content[0], content[1])
