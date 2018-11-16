import time
import asyncio
import logging
import sys

import discord


from reddit.client import Client as Reddit
from utils.lib import (
	get_channel,
	get_channel_messages,
	get_new_posts,
	get_posts_string
)
from utils.servers import SERVERS
from utils.token import TOKEN

INTERVAL = 1800 # look for new posts every 30 minutes

client = discord.Client()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
logger.addHandler(handler)

@client.event
async def on_ready():
	logger.info("client started!")
	client.loop.create_task(main())

async def main():
	while True:
		for server in SERVERS:
			subreddit = server['subreddit']
			posts = server['posts']
			server_name = server['name']
			server_channel = server['channel']
			category = server.get('category', 'hot')

			logger.info(f"looking for new posts for {subreddit} subreddit")
			channel = get_channel(client, server_name, server_channel)
			channel_messages = await get_channel_messages(client, channel, posts)
			reddit_client = Reddit()
			last_reddit_posts = reddit_client.get_posts(subreddit, category, posts)

			new_posts = get_new_posts(channel_messages, last_reddit_posts)
			if new_posts:
				logger.info(f"found {len(new_posts)} new posts")
				for post in new_posts:
					logger.info(f"writing new post message in {channel}")
					post_string = get_posts_string(post)
					await client.send_message(channel, post_string)
				logger.info(f"finished writing new post messages in {channel}")
			else:
				logger.info(f"no new posts found for {subreddit}")

		logger.info(f"sleeping for {INTERVAL} seconds")
		await asyncio.sleep(INTERVAL)

if __name__ == '__main__':
	try:
		logger.info("starting client")
		client.run(TOKEN)
	except KeyboardInterrupt:
		logger.info("shutting down client")
		client.close()
