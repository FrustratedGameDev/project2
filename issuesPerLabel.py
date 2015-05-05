# count num lines with 'action: labeled' and make a bucket for each 'what: {issue-name}'

labels = {}

def countLabels():
    with open('ourRepo.txt') as file:
        for line in file:
            if "action : labeled" in line:
                parts = line.split(',')
                for part in parts:
                    if "what :" in part:
                        label = part.split("what : ")[1]
                        if label not in labels:
                            labels[label] = 1
                        else:
                            labels[label] += 1



countLabels()

sortedLabels = sorted(labels, key=labels.get)

print('label, number of issues')
for label in sortedLabels:
    count = str(labels[label])
    print(label + ", " + count)