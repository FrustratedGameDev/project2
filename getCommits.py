# /repos/:owner/:repo/commits

from __future__ import print_function
import urllib2
import json
import re,datetime
import sys

def dump(u,commits):
  try:
    return dump1(u, commits)
  except Exception as e: 
    print(e)
    print("Contact TA")
    return False

def dump1(u,commits):
  token = "your token here" # <===
  request = urllib2.Request(u, headers={"Authorization" : "token " + token})
  v = urllib2.urlopen(request).read()
  w = json.loads(v)
  if not w: return False
  for event in w:
  	print(event)
  return True

  # Data to keep
  # - sha
  # author
  # commit message
  # time committed

def launchDump():
  page = 1
  commits = dict()
  while(True):
    doNext = dump('https://api.github.com/repos/FrustratedGameDev/Papers/commits?page=' + str(page), commits)
    #print("page "+ str(page))
    page += 1
    if not doNext : break
  for commit, events in commits.iteritems():
    print("COMMIT " + str(commit))
    # TODO sort events based on time
    #sortedEvents = sorted(events, key=lambda k: k['when']) 

    for event in sortedEvents: print(event.show())
    print('')
    
launchDump()