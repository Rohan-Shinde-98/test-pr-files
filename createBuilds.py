import requests

def triggerBuilds(file):
  body={
    "request": {
    "message": "Override the commit message: this is an api request",
    "branch":"master",
    "merge_mode": "deep_merge",
    "config": {
        "env": {
          "jobs": [
            "TEST=unit"
          ]
        },
        "script": file
      }
    }}
  
  headers={
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Travis-API-Version": "3",
    "Authorization": "${{ secrets.AUTH_TOKEN }}"
  }
  
  response = requests.get("https://api.travis-ci.com/repo/travis-ci/travis-core/requests", data=body, headers=headers)
  print(response.json())

  
  
triggerBuilds("echo 'Hello World'")
