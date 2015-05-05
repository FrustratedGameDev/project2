#get the list of contributors from the repo using https://api.github.com/repos/FrustratedGameDev/Papers/contributors?page=

#to run do: python anonymize.py FrustratedGameDev/Papers

# From this list of 'login' assign each person an alias. e.g. person 1 person 2

#this tool should then parse through all other files to use that alias.

from __future__ import print_function
import urllib2
import json
import re,datetime
import sys
#import requests

import fileinput, glob, string, sys, os
from os.path import join

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
#Where path is the dir to ge the files from
# Test command:  python anonymize2.py FrustratedGameDev/Papers /Users/Denae/git/CSC510/project2/testdir

def findanddestroy(path,exts=None):
	#for each file in the directory
    # replace a string in multiple files
   

	print("Is this still the userList? ")
	print(userList)

	files = glob.glob(path + "/*.csv")
	if files is not []:
		for file in files:
			if os.path.isfile(file):
				if exts is None or exts.count(os.path.splitext(file)[1]) is not 0:
					for line in fileinput.input(file,inplace=1):
						for user in userList:
							lineno = 0
	                        lineno = string.find(line, str(user))
	                        if lineno >0:
	                            line = line.replace(str(user), userList[user])
	                        sys.stdout.write(line)
						#for mstone in milestoneList:
	                    #	lineno = 0
	                    #   lineno = string.find(line, str(mstone))
	                    #    if lineno >0:
	                    #        line = line.replace(str(mstone), milestoneList[mstone])t
	                    #    sys.stdout.write(line)

  		


if __name__ == '__main__':
    usercleaner(sys.argv[1])
    milestonecleaner(sys.argv[1])
    findanddestroy(sys.argv[2])
