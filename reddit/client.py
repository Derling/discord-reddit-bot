from reddit.lib import init_client


class Client:
	"""Reddit client for interacting with the reddit api."""
	
	def __init__(self):
		self._client = init_client()

	def get_posts(self, subreddit, category='hot', posts=25):
		""""Get the latests submissions for a subreddit

		Args:
			subreddit(str): the subreddit to get the posts from
			category(str): the category to get the posts from(ie hot, top)

		Returns:
			An array of responses of reddit Submission objects
		"""
		subreddit = self._client.subreddit(subreddit)
		category_callable = getattr(subreddit, category)
		return list(category_callable(limit=posts))
