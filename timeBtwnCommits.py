# 'committer': {'date': 

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

def display():
    for user in userToCommits:
        print("===\n" + user)
        dates = userToCommits[user]
        prev = None
        for date in dates:
            if prev != None:
                print(prev - date)

            prev = date

getCommitsForEachUser()
display()
