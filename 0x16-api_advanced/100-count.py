import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

    :param subreddit: The subreddit name.
    :param word_list: A list of keywords to count.
    :param after: The 'after' parameter for pagination.
    :param counts: A dictionary to store the counts (initially an empty dictionary).
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
            return

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']

            if counts is None:
                counts = {}

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        counts[word] = counts.get(word, 0) + 1

            after = data['data']['after']
            if after:
                count_words(subreddit, word_list, after, counts)
            else:
                print_results(counts)
        else:
            return
    except requests.RequestException as e:
        print(f"Error: {e}")
        return


def print_results(counts):
    """
    Prints the sorted count of keywords.

    :param counts: A dictionary containing keyword counts.
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for keyword, count in sorted_counts:
        print(f"{keyword}: {count}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Please pass arguments for the subreddit and keywords.")
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2:]
        count_words(subreddit, keywords)
