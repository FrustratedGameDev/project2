#getOpenMilestone.py

#TO RUN Do:
#python getopenmilestone.py CSC510/SQLvsNOSQL >results/project_3.csv

#TODO be generate table for Open Milestone
from __future__ import print_function
import urllib2
import json
import re,datetime
import sys
from datetime import datetime
#import requests

import fileinput, glob, string, sys, os
from os.path import join


openStones = {}

def findOpenMilestones(repo):
  site = "https://api.github.com/repos/" +repo+ "/milestones?page=1"
  #resp = urllib2.urlopen(site)
  v = urllib2.urlopen(site).read()
  w = json.loads(v)

 # usercount = 1
  if not w: return False
  for block in w:
    title = block['title']
    openedIssNum = block['open_issues']
    closedIssNum = block['closed_issues']
    duedate = block['due_on']
      
    print(str(title) + "," + str(openedIssNum) + "," + str(closedIssNum) + ","+ str(duedate))

      #userList[user] = "user_"+str(usercount)
      #usercount+=1

if __name__ == '__main__':
    findOpenMilestones(sys.argv[1])