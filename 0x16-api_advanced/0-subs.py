#!/usr/bin/python3
"""Returns number of subscribers for a given subreddit"""


import requests

def number_of_subscribers(subreddit):
    """Queries reddit API and returns
    number of subscribers for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
    except (KeyError, ValueError) as e:
        print(f"Error parsing JSON: {e}")
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = number_of_subscribers(subreddit)
        print("{:d}".format(result))
