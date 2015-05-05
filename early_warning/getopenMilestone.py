#getOpenMilestone.csv

#TODO be generate table for Open Milestone

from __future__ import print_function
import urllib2
import json
import re, datetime
import sys
from datetime import datetime

def findOpenMilestones():
  userToMessageLength = {}

  for commit in allCommits:
    length = len(commit.message)
    if commit.user in userToMessageLength:
      userToMessageLength[commit.user].append(length)
    else:
      userToMessageLength[commit.user] = [length]

  for user in userToMessageLength:
    userToMessageLength[user].sort()

  with open('project_1.csv', 'w') as file:
    file.write('username, length of message\n')
    for user in userToMessageLength:
      for msgLength in userToMessageLength[user]:
        file.write(user + ", " + str(msgLength) + '\n') 

