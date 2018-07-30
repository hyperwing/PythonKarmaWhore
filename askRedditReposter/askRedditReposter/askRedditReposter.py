import praw


client_id = 'kHoe'
client_secret = 'QGwoiJVH1OH92xUrSaP7w9cycKM'
password = 'P@ssw0rd96'
username = 'pyeng'


reddit = praw.Reddit(client_id=client_id,
                     client_secret = client_secret, password = password,
                     user_agent='USERAGENT', username = username)

for subreddit in reddit.subreddits.default(limit=None):
    print(subreddit)