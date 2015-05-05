#get the list of contributors from the repo using https://api.github.com/repos/FrustratedGameDev/Papers/contributors?page=

#to run do: python anonymize2.py FrustratedGameDev/Papers

# From this list of 'login' assign each person an alias. e.g. person 1 person 2

#this tool should then parse through all other files to use that alias.

from __future__ import print_function
import urllib2
import json
import re,datetime
import sys
#import requests

userList = {}
milestoneList = {}

def usercleaner(repo):
	usersite = "https://api.github.com/repos/" +repo+ "/contributors?page=1"
	#resp = urllib2.urlopen(site)
	v = urllib2.urlopen(usersite).read()
  	w = json.loads(v)

	usercount = 1
  	if not w: return False
  	for contributor in w:
  		user = contributor['login']
  		#print(user)
  		userList[user] = "user_"+str(usercount)
  		usercount+=1

  	print("User list: ")
  	print(userList)

# Collects a dict of the alias names
def milestonecleaner(repo):
	milestonesite = "https://api.github.com/repos/"+repo+"/milestones?state=all&page=1"
	v = urllib2.urlopen(milestonesite).read()
  	w = json.loads(v)
	
	milestonecount = 1
	if not w: return False
  	for milestone in w:
  		mstone = milestone['title']
  		#print(mstone)
  		milestoneList[mstone] = "milestone_"+str(milestonecount)
  		milestonecount+=1

  	print("Milestone list: ")
  	print(milestoneList)

#This method finds all the files in the diirectory exposing personal information and changes it to the appopriate names
#def findanddestroy(dir2check):
	#for each file in the directory

  		


if __name__ == '__main__':
    usercleaner(sys.argv[1])
    milestonecleaner(sys.argv[1])
    findanddestroy(sys.argv[2])