# Discord-reddit-bot
A bot that pulls information from a subreddit and posts it in a discord channel

## Requirements

This project was built in an environment using **Python3.6.5** to ensure that this will behave as expected please install the appropriate python version.

[*Nice to have: create a virtual environment for the bot to run in*](https://virtualenvwrapper.readthedocs.io/en/latest/)

**Must Haves**: 
- [A Discord account](https://discordapp.com/)
- [A Reddit account](https://www.reddit.com/)
- [Python 3.6.x](https://www.python.org/downloads/)

Once we have these things installed we need to [clone](https://git-scm.com/docs/git-clone) this project!

## Discord Requirements

### Create a server
If you don't already have a server, create one for free on the [Discord App](https://discordapp.com). Simply log in, and then click the plus on the left side of the main window and create a new server.

### Create an app
Go to the [applications page](https://discordapp.com/developers/applications/me) and create a new app. On your app detail page, save the Client ID. **You will need it later to authorize your bot for your server.** Lets refer to this as the `client_id`

### Create a bot account for your app
After creating the app, on the app details page, scroll down to the section named bot, and create a bot user. **Save the token, you will need it later to run the bot.** Lets refer to this as the `bot_token`

### Authorize the bot for your server
Visit the url https://discordapp.com/oauth2/authorize?client_id=XXXX&scope=bot but replace XXXX with your app `client_id`. Choose the server you want to add it to and select authorize(add it to the one we made earlier or one you belong to where you have admin privileges).

### Add the token
Our discord client needs the bot token to be able to authenticate through the discord client api. Now that we have added our bot to the server we need to be able to log in as the bot. We simply need to add the `bot_token` to our TOKEN.py file. This file lives in the utils folder.

## Reddit Requirements

### Create an app
We need to create an app. To do so go [here](https://www.reddit.com/prefs/apps/) and click `create an app`. Make sure to click **Script** as the type of app.

### Add the Reddit credentials
Just like the discord client our reddit client needs credentials to authenticate. Here we will need your Reddit log in credentials and the client secret and client id of the app we just made. Simply add these values to the cred.py file. This file lives in the reddit folder. We also need a user agent, the convention for reddit scripts is to give it a user agent with the following format "u/{user_name} bot". Where user_name is your reddit user name.

## The subreddits

Go to the servers.py file and add the subreddits that you want to grab posts from and where you want the messages to be written in.

