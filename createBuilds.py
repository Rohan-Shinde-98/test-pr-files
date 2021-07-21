import requests
import os
import json
import threading

def triggerBuilds(fileName, fileURL):
  body={
    "request": {
      "config": {
          "stage": "Testing",
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
  
  response = requests.post("https://api.travis-ci.com/repo/Rohan-Shinde-98%2Ftest-trigger-build/requests", data=json.dumps(body), headers=headers)

  # Polling
  


# Hold the each build threads 
build_threads = []

file_content = open('changed_files.txt','r')
for file in file_content:
  content = file.split()
  triggerBuilds(content[0], content[1])

#   # Create thread for each build
#   t = threading.Thread(target=triggerBuilds, arg=[fileName,fileURL])
#   t.start()
#   build_threads.append(t)

# # Wait for all child builds to finish
# for thread in build_threads:
#   thread.join()

file_content.close()
