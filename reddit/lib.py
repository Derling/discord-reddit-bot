import praw

from .creds import oauth_creds

def init_client():
	"""Returns an instance of the PRAW reddit client"""
	return praw.Reddit(**oauth_creds)
