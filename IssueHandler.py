# count num lines with 'action: ' and make a bucket for each 'user: {user-name}'

users = {}

def countUsers():
    with open('ourRepo.txt') as file:
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



countUsers()

sortedUsers = sorted(users, key=users.get)
print("The list below identifies how much activity each user had on all  issues:\n")

for user in sortedUsers:
    count = str(users[user])
    print(user + "\t" + count)

    #Right now this tool gathers ones that don't have milestones. 
        #This is identified as those with a new line behind it. 

print("\nThe person to close an issue is usually the one that fixed it. The following list identifies the number of issues that a user was the last person to handle the issue:")