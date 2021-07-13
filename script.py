import requests
import sys

def getChangedFiles(TRAVIS_PULL_REQUEST):
  response = requests.get("https://api.github.com/repos/Rohan-Shinde-98/test-pr-files/pulls/"+TRAVIS_PULL_REQUEST+"/files")
  print(response)

if __name__=="__main__":
  getChangedFiles(sys.argv[1])
