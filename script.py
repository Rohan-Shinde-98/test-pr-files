import requests
import sys

def getChangedFiles(TRAVIS_PULL_REQUEST):
  response = requests.get("https://api.github.com/repos/Rohan-Shinde-98/test-pr-files/pulls/"+str(TRAVIS_PULL_REQUEST)+"/files")
#   print(response.text)
  file = open('changed_files.txt','a')
  for object in response.json():
    string = object['filename'] + "\t" + object['raw_url']
    file.write(string)
  file.close()
  file = open('changed_files.txt','r')
  print(file.read())
  file.close()

if __name__=="__main__":
  getChangedFiles(sys.argv[1])
  file = open('changed_files.txt','r')
  print(file.read())
  file.close()
