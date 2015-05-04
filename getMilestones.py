# /repos/:owner/:repo/commits

"""
You will need to add your authorization token in the code.
Here is how you do it.

1) In terminal run the following command

curl -i -u <your_username> -d '{"scopes": ["repo", "user"], "note": "OpenSciences"}' https://api.github.com/authorizations

2) Enter your password on prompt. You will get a JSON response. 
In that response there will be a key called "token" . 
Save the token in a file called token.

3) Run the python file and it will read the file

     python getmilestones.py

"""

from __future__ import print_function
import urllib2
import json
import re,datetime
import sys

file = open('token')
Token = file.read().rstrip()

def dump(u,milestones):
  try:
    return dump1(u, milestones)
  except Exception as e: 
    print(e)
    print("Contact TA")
    return False

def dump1(u,milestones):
  request = urllib2.Request(u, headers={"Authorization" : "token " + Token})
  v = urllib2.urlopen(request).read()
  w = json.loads(v)
  if not w: return False
  for event in w:
  	print(event)
  return True

def launchDump():
  page = 1
  milestones = dict()
  while(True):
    doNext = dump('https://api.github.com/repos/FrustratedGameDev/Papers/milestones?state=all&page=' + str(page), milestones)
    #print("page "+ str(page))
    page += 1
    if not doNext : break
  for milestone, events in milestones.iteritems():
    print("MILESTONE " + str(milestone))
    # TODO sort events based on time
    #sortedEvents = sorted(events, key=lambda k: k['when']) 

    for event in sortedEvents: print(event.show())
    print('')
    
launchDump()