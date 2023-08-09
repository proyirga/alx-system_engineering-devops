#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "X11; Ubuntu; Linux x86_64; rv:109.0 (by /u/proyirga)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_response = response.json()
        data_response = json_response['data']
        subscribers = data_response['subscribers']
        return subscribers
    return 0
