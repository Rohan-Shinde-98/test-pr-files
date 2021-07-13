import requests
import sys

def getChangedFiles(TRAVIS_PULL_REQUEST):
  response = requests.get("https://api.github.com/repos/Rohan-Shinde-98/test-pr-files/pulls/"+str(TRAVIS_PULL_REQUEST)+"/files")
#   print(response.text)
  file = open('changed_files','a')
  for object in response.json():
    file.write(object['filename'] + " " + object['raw_url'])
    print(object['filename'])
    print(object['raw_url'])

if __name__=="__main__":
  getChangedFiles(sys.argv[1])
