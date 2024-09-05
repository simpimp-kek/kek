import requests
import pandas as pd

def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def analyze_repos(repos):
    if not repos:
        return None
    
    data = []
    for repo in repos:
        data.append({
            'name': repo['name'],
            'stars': repo['stargazers_count'],
            'forks': repo['forks_count'],
            'language': repo['language']
        })
    
    df = pd.DataFrame(data)
    return df

def main():
    username = input("Enter a GitHub username: ")
    repos = fetch_github_repos(username)
    if repos:
        df = analyze_repos(repos)
        print(df.head())
        print("\nMost starred repositories:")
        print(df.nlargest(5, 'stars')[['name', 'stars']])
        print("\nLanguage distribution:")
        print(df['language'].value_counts())
    else:
        print("Failed to fetch repositories.")

if __name__ == "__main__":
    main()
