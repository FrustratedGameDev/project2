from __future__ import print_function
import urllib2
import json
import re,datetime
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("repo")
args = parser.parse_args()

def findFirstWeek(weeks):
  start = 0
  for week in weeks:
    if week > 0: break
    start += 1
  return start

def findLastWeek(weeks):
  end = len(weeks) - 1
  while weeks[end] == 0:
    end -= 1
  return end + 1

def trimWeeks(weeks):
  start = findFirstWeek(weeks)
  end = findLastWeek(weeks)
  return weeks[start:end]

def makeRequest(repo):
  url = "https://api.github.com/repos/" + repo + "/stats/participation"
  print(url)
  rawData = urllib2.urlopen(url).read()
  jsonData = json.loads(rawData)

  if not jsonData: return False

  weeks = jsonData['all']

  activeWeeks = trimWeeks(weeks)
  with open('commits-per-week.csv', 'w') as file:
    file.write('week, commits\n')

    i = 1
    for week in activeWeeks:
      file.write(str(i) + ", " + str(week) + '\n')
      i += 1

makeRequest(args.repo)