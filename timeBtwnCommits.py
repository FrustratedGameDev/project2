# 'committer': {'date': 

from datetime import datetime

def getTimeBtwnCommits():
    with open('commit-data.txt') as file:
        for line in file:
            if "'committer': {'date': " in line:
                dateTilEndOfLine = line.split("committer': {'date': ")[1]
                dateWithPunct = dateTilEndOfLine.split(",")[0]
                date = dateWithPunct.replace("'", "")

                date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
                print(date_object)

getTimeBtwnCommits()