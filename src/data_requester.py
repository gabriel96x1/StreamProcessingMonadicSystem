import praw
import json

def request_reddit_data(amount_of_comments, subreddit='androiddev'):
    with open("src/secrets.json") as secrets_file:
        secrets = json.load(secrets_file)

        reddit = praw.Reddit(
            client_id=secrets['client_id'],
            client_secret=secrets['client_secret'],
            user_agent='jutsuNoTendoPainDev',
            username=secrets['username'],
            password=secrets['password']
        )

        subreddit = reddit.subreddit(subreddit)

        print(subreddit.display_name)
        # Output: redditdev
        print(subreddit.title)
        # Output: reddit development
        return subreddit.comments(limit=amount_of_comments)
        