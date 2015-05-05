# count num lines with 'action: ' and make a bucket for each 'user: {user-name}'

issuesWithoutMilestones = []

def countIssuesWithoutMilestones():
    with open('../../ourRepo.txt') as file:
        for line in file:
            if "action :" in line:
                parts = line.split(',')
                for part in parts:
                    if "user :" in part:
                        user = part.split("user : ")[1]
                        if user not in users:
                            users[user] = 1
                        else:
                            users[user] += 1



countIssuesWithoutMilestones()

sortedUsers = sorted(users, key=users.get)
print("The list below identifies how much activity each user had on all  issues:\n")


with open('issue-no-milestone.csv', 'w') as file:
    file.write('user, number of issues handled\n')
    for user in sortedUsers:
        count = str(users[user])
        file.write(user + ", " + count +'\n')

    #Right now this tool gathers ones that don't have milestones. 
        #This is identified as those with a new line behind it. 

print("\nThe person to close an issue is usually the one that fixed it.")
print("The following list identifies the number of issues that a user was the last person to handle the issue:")