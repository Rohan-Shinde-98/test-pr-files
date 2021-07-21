import requests
import os
import json
import threading
from time import sleep

# Holds the build status of each build triggered
build_state = {}

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
  
  # Make a build request
  response = requests.post("https://api.travis-ci.com/repo/Rohan-Shinde-98%2Ftest-trigger-build/requests", data=json.dumps(body), headers=headers)
  #get the response body
  data = response.json()
  # Get the request number to get the build info
  request_no = data["request"]["id"]
  
  
  print("Request Number : ",request_no)
  print("Sleeping..............")
  

#   Make a request to get the build numbers wait some time to spin up the build
  sleep(10)
  response = requests.get("https://api.travis-ci.com/repo/20274855/request/"+str(request_no),headers=headers)  
  #get the build number from the request number
  build_number = response.json()["builds"][0]["id"]
  
  
  print("Build Number ", build_number)
  print("Starting the polllll.....")
  
  
  
#   #Polling the build status
#   while True:
#     response = requests.get("https://api.travis-ci.com/build/"+str(build_number), headers=headers)
#     data = response.json()["state"]
#     if data == "failed" or data == "passed" or data == "canceled":
#       if build_number in build_state:
#         build_state[build_number] = data
#         break
#     sleep(10)
#     print("poling.........")
    
#   print("polling done")
#   print(build_state)

  


# Hold the each build threads 
build_threads = []

file_content = open('changed_files.txt','r')
# print(file_content.read())
for file in file_content:
  content = file.split()
  triggerBuilds(content[0], content[1])
  break

#   # Create thread for each build
#   t = threading.Thread(target=triggerBuilds, arg=[fileName,fileURL])
#   t.start()
#   build_threads.append(t)

# # Wait for all child builds to finish
# for thread in build_threads:
#   thread.join()

file_content.close()
