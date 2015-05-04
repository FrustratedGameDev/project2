GitHub Scraping
===

# Resources
* [Project Description](http://www4.ncsu.edu/~tjmenzie/cs510/posts/project2.html)
* [Rubric](http://www4.ncsu.edu/~tjmenzie/cs510/posts/rubric6.html)

# Features
We need 10-20 features (useful representation of data)
* Number of times each label was used? (done)
	* search for
		* action : labeled
		* what : {issue-name}
	* make count of these
* Mean and standard deviation of times spent in each label?
* "Unusually long" time; i.e. more than, say, mean + 1.5 or 2 standard deviations time in a label
* "Unusually small" number of issues handled by person21?(Denae started but needs refinement)
* "Unusually large" number of commits? (Denae will do) Needs another file(https://developer.github.com/v3/repos/commits/)
* Large time between commits for one person? (in progress - Anthony)
* Length of commit message
* Number of issues per milestone - Denae
* Number of issues without milestone - Denae

# Bad Smells
What bad smells can we detect using the above features?
