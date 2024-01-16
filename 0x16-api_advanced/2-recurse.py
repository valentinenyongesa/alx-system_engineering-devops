import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    :param subreddit: The subreddit name.
    :param hot_list: The list to store titles (initially an empty list).
    :param after: The 'after' parameter for pagination.
    :return: A list containing the titles of all hot articles or None if no results are found.
    """
    if not after:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'

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
                hot_list.append(title)

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
