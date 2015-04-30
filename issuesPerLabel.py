# count num lines with 'action: labeled' and make a bucket for each 'what: {issue-name}'

with open('ourRepo.txt') as file:
    for line in file:
        if "action : labeled" in line:
            print(line)
