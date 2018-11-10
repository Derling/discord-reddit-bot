def get_channel(client, server_name, channel_name):
	"""Get the corresponding discord Channel object.

	Args:
		client(discord.Client): a discord Client object for interacting with the discord api
		server_name(str): the name of the server where the channel lives in
		channel_name(str): the name of the channel

	Returns:
		A discord Channel object
	"""
	for server in client.servers:
		if server.name == server_name:
			for channel in server.channels:
				if channel.name == channel_name:
					return channel
	return None

async def get_channel_messages(client, channel, messages):
	"""Get the latest messages in a channel.

	Args:
		client(discord.Client): a discord Client object for interacting with the discord api
		channel(discord.Channel): a discord Channel object which represents the channel to look into
		message(int): the number of messages to retrieve

	Returns:
		A list of strings that are the last messages that were posted in the channel
	"""
	messages = []
	async for message in client.logs_from(channel, limit=500):
		messages.append(message.content)
	return messages


def parse_messages(messages):
	"""Gets the tiles of the posts from the string of messages

	Args:
		messages(list[str]): a list of messages posted in a discord channel
	"""
	titles = []
	for message in messages:
		# the -1 is for the additional whitespace
		# between the title and the url
		msg_title = message.split('http')[0][:-1]
		titles.append(msg_title)
	return titles

def get_new_posts(messages, posts):
	"""Gets a list of posts that are not in the discord channel

	Args:
		messages(list[str]): a list of messages posted in a discord channel
		posts(list[reddit.Submission]): a list of reddit submission objects

	Returns:
		A list of strings that 
	"""
	titles =  parse_messages(messages)
	new_posts = []
	for post in posts:
		if post.title not in titles:
			new_posts.append(post)
	return new_posts


def get_posts_string(post):
	"""Get a string that can be posted to a discord channel

	Args:
		post(reddit.Submission): a reddit submission object

	Returns:
		A string of the title of the post followed by the url of the post
	"""
	return f'{post.title} {post.url}'