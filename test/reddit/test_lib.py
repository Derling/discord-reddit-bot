import mock

from reddit.lib import init_client

def test_init_client_returns_correct_user():
	with mock.patch('reddit.lib.praw.Reddit') as reddit_patch:
		user_mock = mock.Mock
		user_mock.name = mock.Mock(return_value='fake_user')
		client = init_client()
		assert client.user().name() == 'fake_user'

