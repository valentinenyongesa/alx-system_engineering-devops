import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    :param subreddit: The subreddit name.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        if 'error' in data:
            print(f"Error: {data['error']}")
            return None

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print("No posts found.")
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
