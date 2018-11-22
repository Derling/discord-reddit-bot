import pytest
from mock import patch, Mock

from utils.lib import (
	get_channel,
	parse_messages,
	get_new_posts,
	get_posts_string
)


servers = [
	{
		'name': 'server1',
		'channels': ['chan1', 'chan2']
	},
	{
		'name': 'server2',
		'channels': ['channel1', 'channel2']
	},
	{
		'name': 'server3',
		'channels': ['general']
	}
]


def get_mock_client():
	mock_client = Mock()
	mocked_servers = []
	for server in servers:
		mock_server = Mock()
		mock_server.name = server['name']

		mock_channels = []
		for channel in server['channels']:
			mock_channel = Mock()
			mock_channel.name = channel
			mock_channels.append(mock_channel)
		mock_server.channels = mock_channels

		mocked_servers.append(mock_server)
	
	mock_client.servers = mocked_servers

	return mock_client


def test_get_channel_returns_correct_channel():
	client = get_mock_client()
	server = 'server1'
	channel = 'chan1'

	assert get_channel(client, server, channel).name == channel


def test_get_channel_raises_error_when_client_doesnt_belong_to_expected_server():
	client = get_mock_client()
	server = 'fake_server'
	channel = 'channel'

	with pytest.raises(Exception) as error:
		get_channel(client, server, channel)
	assert str(error.value) == "Client does not belong to the fake_server server"


def test_get_channel_raises_error_when_client_belongs_to_server_but_invalid_channel_is_provided():
	client = get_mock_client()
	server = 'server1'
	channel = 'fake_channel'

	with pytest.raises(Exception) as error:
		get_channel(client, server, channel)
	assert str(error.value) == "Client belongs to server1 server but could not " \
						 	   "find the fake_channel channel in the server"


def test_parse_messages_returns_correct_strings():
	assert parse_messages([
		'title1 http://url_for_post',
		'title2 http://url_for_second_post']
	) == ['title1', 'title2']


def test_get_new_posts_returns_new_posts():
	old_posts = []
	for title in ['old1', 'old2']:
		mock_post = Mock()
		mock_post.title = title
		old_posts.append(mock_post)
	
	messages = [f'{p.title} http://url' for p in old_posts]
	
	new_posts = []
	for title in ['new1', 'new2']:
		mock_post = Mock()
		mock_post.title = title
		new_posts.append(mock_post)

	assert get_new_posts(messages, old_posts + new_posts) == new_posts


def test_get_posts_string_returns_correct_post_string():
	mock_post = Mock()
	mock_post.title = 'Mock Title For An Awesome Post'
	mock_post.url = 'http://url.for/awesome_post'

	assert get_posts_string(mock_post) == 'Mock Title For An Awesome Post http://url.for/awesome_post'
