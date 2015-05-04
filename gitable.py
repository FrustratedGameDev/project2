#  gitabel
#  the world's smallest project management tool
#  reports relabelling times in github (time in seconds since epoch)
#  thanks to dr parnin
#  todo:
#    - ensure events sorted by time
#    - add issue id
#    - add person handle

"""
You will need to add your authorization token in the code.
Here is how you do it.

1) In terminal run the following command

curl -i -u <your_username> -d '{"scopes": ["repo", "user"], "note": "OpenSciences"}' https://api.github.com/authorizations

2) Enter ur password on prompt. You will get a JSON response. 
In that response there will be a key called "token" . 
Copy the value for that key and paste it on line marked "token" in the attached source code. 

3) Run the python file. 

     python gitable.py

"""
 
from __future__ import print_function
import urllib2
import json
import re,datetime
import sys
import math

file = open('token')
Token = file.read().rstrip()
 
class L():
  "Anonymous container"
  def __init__(i,**fields) : 
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i
  def __repr__(i):
    d = i.__dict__
    name = i.__class__.__name__
    return name+'{'+' '.join([':%s %s' % (k,pretty(d[k])) 
                     for k in i.show()])+ '}'
  def show(i):
    lst = [str(k)+" : "+str(v) for k,v in i.__dict__.iteritems() if v != None]
    return ',\t'.join(map(str,lst))

  def __getitem__(i, item):
    return i.__dict__['when']


  
def secs(d0):
  d     = datetime.datetime(*map(int, re.split('[^\d]', d0)[:-1]))
  epoch = datetime.datetime.utcfromtimestamp(0)
  delta = d - epoch
  return delta.total_seconds()
 
def dump1(u,issues):
  token = "6549e71a0724c93d6f233051d99de248fff5bff8" # <===
  request = urllib2.Request(u, headers={"Authorization" : "token " + Token})
  v = urllib2.urlopen(request).read()
  w = json.loads(v)
  if not w: return False
  for event in w:
    issue_id = event['issue']['number']
    if not event.get('label'): continue
    created_at = secs(event['created_at'])
    action = event['event']
    label_name = event['label']['name']
    user = event['actor']['login']
    milestone = event['issue']['milestone']
    if milestone != None : milestone = milestone['title']
    eventObj = L(when=created_at,
                 action = action,
                 what = label_name,
                 user = user,
                 milestone = milestone)
    all_events = issues.get(issue_id)
    if not all_events: all_events = []
    all_events.append(eventObj)
    issues[issue_id] = all_events
  return True

def dump(u,issues):
  try:
    return dump1(u, issues)
  except Exception as e: 
    print(e)
    print("Contact TA")
    return False

def launchDump():
  page = 1
  issues = dict()
  while(True):
    doNext = dump('https://api.github.com/repos/FrustratedGameDev/Papers/issues/events?page=' + str(page), issues)
    print(page)
    page += 1
    if not doNext : break

  timePerLabel = {}

  with open('label-durations.txt', 'w') as file:
    for issue, events in issues.iteritems():
      #print("ISSUE " + str(issue))
      # TODO sort events based on time
      sortedEvents = sorted(events, key=lambda k: k['when']) 

      prevTime = None

      for event in sortedEvents: 
        #print(event.show())
        start = int(event.when)
        #print("when: " + str(start))
        if prevTime == None:
          prevTime = start
        else:
          duration = start - prevTime

          # add to dict
          label = event.what
          if label in timePerLabel:
            timePerLabel[label] += duration
          else:
            timePerLabel[label] = duration

    # remove really small outliers (under 1 second)
    for label, duration in timePerLabel.items():
      if duration < 1000:
        del timePerLabel[label]

    sumNormal = 0
    sumOfSquares = 0;
    file.write('label, time in label (ms)\n')
    for label in timePerLabel:
      file.write(label + ", " + str(timePerLabel[label]) + '\n')
      sumNormal += timePerLabel[label]
      sumOfSquares += timePerLabel[label]**2

    mean = sumNormal / len(timePerLabel)
    file.write('===\n')
    file.write('Mean time per label: ' + str(mean) + '\n')

    num = len(timePerLabel)
    top = math.sqrt(num * sumOfSquares - sumNormal)
    standardDeviation = top / len(timePerLabel)

    file.write('Standard deviation: ' + str(standardDeviation) + '\n')


    
launchDump()
