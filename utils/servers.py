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

Example: 

In this example the bot will pull the last 100 posts from the hot "popular" category from the funny subreddit.
It will then write messages about the posts in the "server-name" server in the "channel-name" channel.
Where "server-name" and "channel-name" would be the actual names for the server and channel the bot belongs to.

SERVERS = [
	{
		'subreddit': 'Funny',
		'posts': 100,
		'category': 'popular',
		'name': 'server-name',
		'channel': 'channel-name'
	}
]
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