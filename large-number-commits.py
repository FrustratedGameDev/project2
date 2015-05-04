from datetime import datetime

userToCommits = {}

def isLineValid(line):
  return "2015" in line and "by " in line

def addToDict(user, date):
  if user not in userToCommits:
    userToCommits[user] = [date] # new list with one element
  else:
    userToCommits[user].append(date)

def getCommitsForEachUser():
  with open('commit-data.txt') as file:
    for line in file:
      if isLineValid(line):
        # get user
        user = line.split('\t')[1].split(' ')[1]
        date = datetime.strptime(line.split('\t')[0], '%Y-%m-%d at %H:%M:%S')
        addToDict(user, date)

def findNumberOfCommitsPerUser():
  with open('large-number-commits.txt', 'w') as file:
    file.write('user, commits\n')
    for user in userToCommits:
      count = len(userToCommits[user])
      file.write(user + ", " + str(count) + '\n')

getCommitsForEachUser()
findNumberOfCommitsPerUser()