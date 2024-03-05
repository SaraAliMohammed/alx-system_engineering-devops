#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers={'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/sara_ali2024)'}
    # Make a GET request to the API with a custom User-Agent
    data = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if data.status_code == 200:
        # Parse the JSON response to get the number of subscribers
        return data.json().get('data').get('subscribers')
    else:
        # Invalid subreddit or other error, return 0
        print(f"Error: {data.status_code}")
        return 0
