#!/bin/sh

#Runs the issue Handler
python issueHandler.py

#Gets the commits from each users
python getCommits.py

#Prints all the Milestones
python getMilestones.py

#anonyizes groups
#anonymizes users within groups
#anonymizes milestones within groups
#Test command:  python anonymize.py FrustratedGameDev/Papers /Users/Denae/git/CSC510/project2/testdir
python anonymize 