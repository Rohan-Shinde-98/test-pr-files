import requests
import sys

def getChangedFiles(TRAVIS_PULL_REQUEST):
  response = requests.get("https://api.github.com/repos/Rohan-Shinde-98/test-pr-files/pulls/"+str(TRAVIS_PULL_REQUEST)+"/files")
  
  file = open('changed_files.txt','a')
  for object in response.json():
    string = object['filename'] + " " + object['raw_url'] +"\n"                     
    file.write(string)
  file.close()

if __name__=="__main__":
  getChangedFiles(sys.argv[1])
