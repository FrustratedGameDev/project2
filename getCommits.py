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

     python getCommits.py

"""

from __future__ import print_function
import urllib2
import json
import re, datetime
import sys
from datetime import datetime

file = open('token')
Token = file.read().rstrip()

allCommits = []

class Commit():
  "Anonymous container"
  def __init__(i,**fields) : 
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i
  def __repr__(i):
    dateStr = datetime.strftime(i.date, '%Y-%m-%d at %H:%M:%S')
    return dateStr + "\tby " + i.user + "\tmessage: " + i.message

  def __getitem__(i, item):
    return i.__dict__['date']

def dump(u,commits):
  try:
    return dump1(u, commits)
  except Exception as e: 
    print(e)
    print("Contact TA")
    return False

def dump1(u,commits):
  request = urllib2.Request(u, headers={"Authorization" : "token " + Token})
  v = urllib2.urlopen(request).read()
  w = json.loads(v)
  if not w: return False
  for commit in w:
    date = datetime.strptime(commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')
    user = commit['author']['login']
    message = commit['commit']['message']

    commitObj = Commit(date=date,
                 user = user,
                 message = message)

    allCommits.append(commitObj)

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
    page += 1
    if not doNext : break

def findMessageLengths():
  userToMessageLength = {}

  for commit in allCommits:
    length = len(commit.message)
    if commit.user in userToMessageLength:
      userToMessageLength[commit.user].append(length)
    else:
      userToMessageLength[commit.user] = [length]

  for user in userToMessageLength:
    userToMessageLength[user].sort()

  with open('message-length.csv', 'w') as file:
    file.write('username, length of message\n')
    for user in userToMessageLength:
      for msgLength in userToMessageLength[user]:
        file.write(user + ", " + str(msgLength) + '\n') 
    
launchDump()
findMessageLengths()

#for commit in allCommits:
  #print(commit)   
