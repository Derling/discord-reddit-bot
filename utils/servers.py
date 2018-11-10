"""
Servers are declared as dictionaries

keys for the dictionaries:
subreddit, posts, category, name, channel

subreddit(str): the subreddit to get the posts from
posts(int): the number of posts to pull from the subreddit
category(str): the reddit category to look at 
			   when pulling posts(defaults to "hot")
name(str): the name of the server
channel(str): the name of the channel
"""

SERVERS = [
	{
		'subreddit': '',
		'posts': 0,
		'category': '',
		'name': '',
		'channel': ''
	}
]