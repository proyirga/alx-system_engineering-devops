#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the 
titles of the first 10 hot posts listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    Args:
        subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)i
    headers = {
        "User-Agent": "X11; Ubuntu; Linux x86_64; rv:109.0 (by /u/proyirga)"
    }
    params = {'limit': '10'}
    response = get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    children = response.json().get('data').get('children')

    for child in children:
        print(child.get('data').get('title'))
