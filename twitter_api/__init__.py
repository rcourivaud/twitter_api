import time
import tweepy

from twitter_api.twitter_user import TwitterUser


class TwitterAPI:
    def __init__(self, consumer_key,
                 consumer_secret,
                 access_token,
                 access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(self.auth)

    def get_user_by_name(self, user_name):
        try:
            return self.api.get_user(user_name)
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

    def get_user_data(self, user_name, db=None):
        return TwitterUser(self.get_user_by_name(user_name=user_name)).get_data(db=db)
