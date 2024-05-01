# GitStats
Find stats for people and repositories on GitHub

### How to use:
#### User search:
First, change the 'username' varible to the **exact** username of the person you want to search. 
Then, paste a 
```python
print(get_github_user_stats(username))
```
into your code.
After that, run the code and it will show you user stats that include:
* Users name
* Users bio
* Number of public repositories the user has
* Follower count
* Following count

#### Repository basic stats:
First, change the 'username' varible to the **exact** username of the person who owns the repository you want to look up.
Then, change the 'repo_name' variable to the **exact** name of the repository.
After your done that, add a 
```python
print(get_github_repo_stats(username, repo_name))
```
to your code, and it will log these repository stats to the console:
* Name of the repository
* Description of the repository
* How many stars the repository has
* How many forks have been made
* And a count of open issues

#### Repository advanced stats:
First, change the 'username' varible to the **exact** username of the person who owns the repository you want to look up.
Then, change the 'repo_name' variable to the **exact** name of the repository.
Add a 
```python
print(get_github_repo_stats_extended(username, repo_name))
```
Run the code and you will get the repository's:
* Name
* Description
* Amount of stars
* Amout of forks
* Open Issue count
* Watchers count
* Language
* License
* Date created
* Date repositroy was pushed at
* URL to clone repository
* Repository size
* Default branch
* Network count

### That is so far all that it can do, more features will be added, so follow for updates
