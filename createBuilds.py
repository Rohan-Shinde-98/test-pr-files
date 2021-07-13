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
  print(body)

  
  
triggerBuilds("test")
