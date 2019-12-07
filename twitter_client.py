import tweepy
from tweepy import OAuthHandler
from config import Config

class TwitterClient(Config):
    """
    Generic Twitter Class for performing sentiment analysis
    """
    def __init__(self, account_name):
        super(TwitterClient, self).__init__()   
        self.account_name = account_name 

        # Attempt Authentication
        try:
            self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
            self.auth.set_access_token(self.access_token, self.access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")


def main():
    ACCOUNT_NAME = 'POTUS'
    tc = TwitterClient(ACCOUNT_NAME)
    print(tc.access_token)

if __name__ == '__main__':
    main() 