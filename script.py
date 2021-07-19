import requests
import sys

def getChangedFiles(TRAVIS_PULL_REQUEST):
  response = requests.get("https://api.github.com/repos/Rohan-Shinde-98/test-pr-files/pulls/"+str(TRAVIS_PULL_REQUEST)+"/files")
  
  #remove line
  print(response.json())
  
  file = open('changed_files.txt','a')
  for object in response.json():
    
    #remove below lines
    string = object['filename'] + "\t" + object['raw_url']
    print(object['filename'], object['raw_url']                                     
    print(string)
    
    file.write(string)
  file.close()
  
  #remove below code
  f = open('changed_files.txt','r')
  print(f.readline())
  f.close()

if __name__=="__main__":
  getChangedFiles(sys.argv[1])
