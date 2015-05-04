# count num lines with 'action: labeled' and make a bucket for each 'what: {issue-name}'

# set of all users, each with a list of times
activity = {}

def isLineData(line):
    return "user : " in line

def recreateActivityLogForUser(user):
    # get all lines with this user
    # put into bucket
    # sort bucket by time

    with open('ourRepo.txt') as file:
        for line in file:
            if isLineData(line) and user in line:
                details = line.split(',')
                for detail in details:
                    label = detail.split("what : ")[1]
                    if label not in labels:
                        labels[label] = 1
                    else:
                        labels[label] += 1

