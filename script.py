import requests
import sys

def getChangedFiles(TRAVIS_PULL_REQUEST):
  response = requests.get("https://api.github.com/repos/Rohan-Shinde-98/test-pr-files/pulls/"+str(TRAVIS_PULL_REQUEST)+"/files")
  print(response.text)
  for object in response.text:
    print(object["sha"])
#     print(object.filename)
#     print(object.status)
#     print(object.modified)
#     print(object.additions)
#     print(object.deletions)
#     print(object.changes)
#     print(object.blob_url)
#     print(object.raw_url)
#     print(object.contents_url)
#     print(object.patch)

if __name__=="__main__":
  getChangedFiles(sys.argv[1])
