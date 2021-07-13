import requests
import sys

def getChangedFiles(TRAVIS_PULL_REQUEST):
  response = requests.get("https://api.github.com/repos/Rohan-Shinde-98/test-pr-files/pulls/"+str(TRAVIS_PULL_REQUEST)+"/files")
#   print(response.text)
  for object in response.json():
    print(object['sha'])

if __name__=="__main__":
  getChangedFiles(sys.argv[1])
