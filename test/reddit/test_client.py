import mock
import pytest

from reddit.client import Client

Client = mock.MagicMock(Client)

mock_api_structure = {
	'subreddits': ['sub1'],
	'sub1': {
		'submissions': {
			'hot': [
				f'sub1_hot{str(i)}' for i in range(100)
			],
			'top': [
				f'sub1_top{str(i)}' for i in range(100)
			]
		}
	}
}


def mock_get_posts(subreddit, category='hot', posts=25):
	# function signature matches the Client object signature
	if subreddit not in mock_api_structure:
		raise Exception('401 error subreddit not found')
	return mock_api_structure[subreddit]['submissions'][category][:posts]


def test_client_returns_correct_hot_submissions():
	client = Client()
	client.get_posts.side_effect = mock_get_posts
	expected_results = mock_api_structure['sub1']['submissions']['hot'][:25]

	assert client.get_posts('sub1') == expected_results


def test_client_returns_correct_top_submissions():
	client = Client()
	client.get_posts.side_effect = mock_get_posts
	expected_results = mock_api_structure['sub1']['submissions']['top'][:25]

	assert client.get_posts('sub1', 'top') == expected_results


def test_client_raises_error_on_nonexistent_submission():
	with pytest.raises(Exception) as subreddit_not_found_exception:
		client = Client()
		client.get_posts.side_effect = mock_get_posts
		client.get_posts('not_a_real_subreddit')

		assert '401' in subreddit_not_found_exception.value
