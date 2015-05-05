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
## 4. Data
### 4.1. Data Samples
## 5. Feature Detection
### 5.1. Feature Detection Results 
## 6. Bad Smells Detector
### 6.1. Bad Smells Results

## 7. Early Warning
 An early warning of a bad smell is being able to detect whether or not people still have milestones open at this stage of projects. 
As we are now in Project 2 and have completed Project1 several weeks ago, the milestones in Project 1 should have been completed as well. 
To search for this we were able to call for all the milestones from a particular repository using:

```https://api.github.com/repos/" + repo + "/milestones?page=1```

We intentionally expected for this call to gather the entire list of milestones for the original project but this only gathered those milestones that are still open.
## 7.1. Early Warning Results
