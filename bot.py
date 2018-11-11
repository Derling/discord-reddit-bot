import discord
import time
import asyncio

from reddit.client import Client as Reddit
from utils.lib import (
	get_channel,
	get_channel_messages,
	get_new_posts,
	get_posts_string
)
from utils.servers import SERVERS
from utils.token import TOKEN

POKE_INTERVAL = 1800 # look for new posts every 30 minutes
client = discord.Client()

@client.event
async def on_ready():
	client.loop.create_task(main())

async def main():
	while True:
		for server in SERVERS:
			subreddit = server['subreddit']
			posts = server['posts']
			server_name = server['name']
			server_channel = server['channel']
			category = server.get('category', 'hot')

			channel = get_channel(client, server_name, server_channel)
			channel_messages = await get_channel_messages(client, channel, posts)
			reddit_client = Reddit()
			last_reddit_posts = reddit_client.get_posts(subreddit, category, posts)

			new_posts = get_new_posts(channel_messages, last_reddit_posts)
			if new_posts:
				for post in new_posts:
					post_string = get_posts_string(post)
					await client.send_message(channel, post_string)

		asyncio.sleep(POKE_INTERVAL)

if __name__ == '__main__':
	try:
		client.run(TOKEN)
	except KeyboardInterrupt:
		client.close()
