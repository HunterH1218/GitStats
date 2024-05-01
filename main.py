import requests

username = "HunterH1218"  # Change to the GitHub username you want to lookup
repo_name = "MagicNet"  # Example repository name
def get_github_user_stats(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        return {
            'name': user_data.get('name'),
            'bio': user_data.get('bio'),
            'public_repos': user_data.get('public_repos'),
            'followers': user_data.get('followers'),
            'following': user_data.get('following')
        }
    else:
        return "User not found or an error occured."



def get_github_repo_stats(username1, repo_name):
    url = f"https://api.github.com/repos/{username1}/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        repo_data = response.json()
        return {
            'name': repo_data.get('name'),
            'description': repo_data.get('description'),
            'stars': repo_data.get('stargazers_count'),
            'forks': repo_data.get('forks_count'),
            'open_issues': repo_data.get('open_issues_count')
        }
    else:
        return "Repository not found or an error occurred."



def get_github_repo_stats_extended(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        repo_data = response.json()
        return {
            'name': repo_data.get('name'),
            'description': repo_data.get('description'),
            'stars': repo_data.get('stargazers_count'),
            'forks': repo_data.get('forks_count'),
            'open_issues': repo_data.get('open_issues_count'),
            'watchers_count': repo_data.get('watchers_count'),
            'language': repo_data.get('language'),
            'license': repo_data.get('license', {}).get('name') if repo_data.get('license') else 'No license',
            'created_at': repo_data.get('created_at'),
            'pushed_at': repo_data.get('pushed_at'),
            'clone_url': repo_data.get('clone_url'),
            'size': repo_data.get('size'),
            'default_branch': repo_data.get('default_branch'),
            'network_count': repo_data.get('network_count')
        }
    else:
        return "Repository not found or an error occurred."
