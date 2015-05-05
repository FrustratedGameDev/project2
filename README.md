  # Project 2 Report
##BadSmell Detector
Anthony Elliott and Denae Ford

May 4, 2014

##  1. Collection

Data was collected using Python scripts.
We started with the intial file given for the study gitable.py and began to build from there.
Using this file as a starter we were able to define other features to extract and allowed us to get acclimated to using the Github API, JSON, and how to write good Python code.
The code created for each feature can be found in a single python file.
The features are divided amongst folder and the data for the three repositories are listed in the feature results folder under their aliases(as assigned by us).


## 2. Anonymized
 To anonymize the data we created a python script that collects the repository specific information(contributors, milestones, etc.) and creates a dictionary linking to those values.
 This dictionary is created for each repository. 
 We created a shell script that then for that specific organization it goes into the result files and pulls all the identifying information out and replaces it with aliases.
 The full code for this is can be found in [anonymized.py](https://github.com/FrustratedGameDev/project2/blob/master/anonymize.py).
 
 ```
 def usercleaner(repo):
	usersite = "https://api.github.com/repos/" +repo+ "/contributors?page=1"
	v = urllib2.urlopen(usersite).read()
  	w = json.loads(v)

	usercount = 1
  	if not w: return False
  	for contributor in w:
  		user = contributor['login']
  		userList[user] = "user_"+str(usercount)
  		usercount+=1

# Collects a dict of the alias names
def milestonecleaner(repo):
	milestonesite = "https://api.github.com/repos/"+repo+"/milestones?state=all&page=1"
	v = urllib2.urlopen(milestonesite).read()
  	w = json.loads(v)
	
	milestonecount = 1
	if not w: return False
  	for milestone in w:
  		mstone = milestone['title']
  		milestoneList[mstone] = "milestone_"+str(milestonecount)
  		milestonecount+=1
 ```
 

## 3. Tables

The tables listed in this projecte were originally redirected output and put into text files. 
During the anonymization process the files were stripped of personal information and converted to csv files.
Statistical measures like the mean and standard deviation of the data set were extracted.
The tables are found in the results folder for each feature and bad smell. 

## Data

The following table demonstrates how much data was collect for each feature.

|Number|Feature|Project1|Project2|Project3|
|------|-------|--------|--------|--------|
|1|Commit Message Length|162|1|1|
|2|Uneven Time Between Commits|160|1|1|
|3|Time per label|19|1|1|
|4|Number of Commits per week|11|1|1|
|5|Uneven number of commits|3|1|1|
|6|Unusual time in Label|1|1|1|
|7|Mean St Dev in Label|2|1|1|
|8|Issues per user|3|1|1|
|9|Number of Issues per milestone|X|1|1|
|10|Issues without Milestones|X|1|1|

##Features

The following are features that we have extraced, the sample data, and badsmells that were detected.

### Feature 1: Commit Message Length
We wanted to extract the length of each commit message.


#### Sample data table:

|username|length of message|
|------|-------|
|person1|14|
|person1|16|
|person2|20|

#### Results

### Feature 2: Uneven Time Between Commits
We wanted to determine how long each contributor went in between each commit. This could be used to help analyze participation.

  #### Sample data table:

|user| time|
|------|-------|
|person1| 3 days; 22:47:26 |
|person2| 0:19:16|

#### Results


### Feature 3: Time per label
We wanted to see how how long issues remained in each label. This could help us determine how the labels were used.

  #### Sample data table:

|label| time in label (ms)|
|------|-------|
|Key article| 2716844|
|Step 1: Relevant Paper| 92355362|

  #### Results

### Feature 4: Number of Commits per week
Finding the number of commits per week could help us determine which people were participating and not. Also, it could help us spot gaps in participation.

#### Sample data table:

Week | Commits
--- | ---
1 | 5
2 | 20

#### Results

### Feature 5: Uneven number of commits
Finding out how many commits each participant created could be a big factor in overall participation. There are other factors behind participation than just commit count, but it could play a factor.

#### Sample data table:

user| commits
--- | ---
person1| 112
person2| 49

#### Results

### Feature 6: Unusual time in Label
Some issues spent an unusually time in some labels.  We wanted to find out how much time an issue spent in each label.


####Sample data table:

label| duration (ms)
--- | ---
Step 1: Relevant Paper| 92355362

#### Results

### Feature 7: Mean St Dev in Label
We also wanted some way to represent the middle of how much time was spent in each label. Additionally, we also wanted to find out how spread out the times were.  The mean and standard deviation fit in well here.

#### Sample data table:

Metric | time (ms)
--- | ---
Mean time per label| 31772392
Standard deviation| 45054088.4484

#### Results


### Feature 8: Issues per user
Commits are one way of measuring participation, measuring how involved a user was in the issues is another way of measuring participation.


#### Sample data table:

user| number of issues handled
--- | ---
person1| 58
person2| 237

#### Results

## Feature 9: Number of Issues per milestone
We wanted to see how many issues were assigned to each milestone. Were they fairly evenly distributed or was there a lot of spread?

#### Sample data table:

milestone | number of issues
--- | ---
milestone1 | 10
milestone2 | 1

#### Results

### Feature 10: Issues without Milestones
In addition to the previous feature, we also want to see how many issues were not assigned to a milestone.

#### Results
Not done yet.

## Early Warning
 An early warning of a bad smell is being able to detect whether or not people still have milestones open at this stage of projects. 
As we are now in Project 2 and have completed Project1 several weeks ago, the milestones in Project 1 should have been completed as well. 
To search for this we were able to call for all the milestones from a particular repository using:

```https://api.github.com/repos/" + repo + "/milestones?page=1```

We intentionally expected for this call to gather the entire list of milestones for the original project but this only gathered those milestones that are still open. 
The code for this tool can be found in [getOpenedMilestones.py](https://github.com/FrustratedGameDev/project2/blob/master/early_warning/getopenMilestone.py).

## Early Warning Results

The early warning result showed that 2 out of the 3 projects had open milestones.
This demonstrates a couple charactersitics about that project: 

1. The team did not finish all they intended for the project. They should have scoped the project better.

2. The team did not have an intense process of closing milestones. They should have a discussed plan of attack that they stuck to.

3. The team is not fully aware of the process of closing milestones and their value.

Here is an example of how the data is set up in the csv files:

|milestone name|open issues|closed issues|due date|
|------|-------|--------|--------|
|milestone_2|5|5|015-04-05T04:00:00Z|

The tables for these findings can be found in [early warning](https://github.com/FrustratedGameDev/project2/tree/master/early_warning).

###Project 1

```
No milestones were detected.
```
[Project 1](https://github.com/FrustratedGameDev/project2/blob/master/early_warning/results/project_1.csv) like many other groups in the class list have not milestones open. 
This demonstrates that the members of this team understood the task at hand and knew how to take advantage of the milestones features.

###Project 2
For [Project 2](https://github.com/FrustratedGameDev/project2/blob/master/early_warning/results/project_2.csv) there were 2 milestones. 
Each of these milestones had no open issues.
One of the milestone had 8 closed issues however which indicated that there was some understanding of the milestones feature and how it correlates with issues. 
This supports the first characteristic listed that the members of the project did not have a good understanding of the scope. 
These milestones listed are also extremely past their March 26 and and 31st dates.

###Project 3
The results for [Project 3](https://github.com/FrustratedGameDev/project2/blob/master/early_warning/results/project_3.csv) show that one of the milestones that was left open did not have any opened issues, closed issues, nor a due date. 
This demonstrates the the team members did not need this Milestone or did not reach the part in the project where the milestone was important.
The second opened milestone for this project had 23 closed issues and no open issues.  
This demonstrates that they were actively using the system but did not recall to close the milestone.  
The due date for the second milestone is also over due by a month as the due date is April 5.

