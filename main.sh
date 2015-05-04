#!/bin/sh

#anonyizes groups
#anonymizes users within groups
#anonymizes milestones within groups

#Runs the issue Handler
python issueHandler.py

#Gets the commits from each users
python getCommits.py

#Prints all the Milestones
python getMilestones.py