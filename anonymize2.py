#get the list of contributors from the repo using https://api.github.com/repos/FrustratedGameDev/Papers/contributors?page=

#to run do: python anonymize2.py FrustratedGameDev/Papers

# From this list of 'login' assign each person an alias. e.g. person 1 person 2

#this tool should then parse through all other files to use that alias.

import urllib2
import sys
#import requests

userList = {}
userLista = {}



def usercleaner(repo):
	site = "https://api.github.com/repos/" +repo+ "/contributors?page=1"
	resp = urllib2.urlopen(site)

	#r = requests.get(site, stream=True)

	for line in resp:
	    	#print line
		if "login" in line:
		    		username = line.split(':')[1]
		        	if username not in userList:
		        	    userList[username] = 1
	#print thing
	#resp = urllib2.urlopen(thing).readlines()
	#for line in webp:
       
                    #else:
                     #   labels[label] += 1

	#TODO find all lines that say user and save the name




	for username in userList:
		print username


if __name__ == '__main__':
    usercleaner(sys.argv[1])