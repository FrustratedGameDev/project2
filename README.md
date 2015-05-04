GitHub Scraping
===

# Resources
* [Project Description](http://www4.ncsu.edu/~tjmenzie/cs510/posts/project2.html)
* [Rubric](http://www4.ncsu.edu/~tjmenzie/cs510/posts/rubric6.html)

# Features
We need 10-20 features (useful representation of data)
1. Number of times each label was used? (done)
	* search for
		* action : labeled
		* what : {issue-name}
	* make count of these
2. Mean and standard deviation of times spent in each label?
3. "Unusually long" time; i.e. more than, say, mean + 1.5 or 2 standard deviations time in a label
4. "Unusually small" number of issues handled by person21?(Denae started but needs refinement)
5. "Unusually large" number of commits? (Denae will do) Needs another file(https://developer.github.com/v3/repos/commits/)
6. Large time between commits for one person? (done)
	* Recreate activity log for each user
	* find time between each event
7. Length of commit message (in progress - Anthony)
8. Number of issues per milestone - Denae
9. Number of issues without milestone - Denae
10. Number of commits per week

# Bad Smells
What bad smells can we detect using the above features?
1. Large number of commits close to a milestone deadline
2. Were there labels that were only used once?
