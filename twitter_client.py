import tweepy
from tweepy import OAuthHandler
from config import Config
from visualise import Visualiser
import re
from textblob import TextBlob 


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

    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        cleaned = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())             
        return cleaned

    def get_tweet_sentiment(self, tweet, ternarised=True): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if ternarised:
            if analysis.sentiment.polarity > 0: 
                return 'positive'
            elif analysis.sentiment.polarity == 0: 
                return 'neutral'
            else: 
                return 'negative'
        else:
            return analysis.sentiment.polarity

    def get_most_recent_tweets(self, tweet_count, ternarised=False):
        recent = self.api.user_timeline(id=self.account_name, count=tweet_count)
        tweets = []

        for id, t in enumerate(recent):
            tweet_info = {}
            tweet_info['id'] = id
            tweet_info['text'] = t.text
            tweet_info['date'] = t.created_at
            tweet_info['cleaned'] = self.clean_tweet(t.text)
            tweet_info['sentiment'] = self.get_tweet_sentiment(t.text, ternarised=ternarised)
            tweets.append(tweet_info)
 
        return tweets


def main():
    ACCOUNT_NAME = 'POTUS'
    TWEET_COUNT = 1000
    AVERAGE = 5
    tc = TwitterClient(ACCOUNT_NAME)
    vs = Visualiser(ACCOUNT_NAME)
    recent = tc.get_most_recent_tweets(TWEET_COUNT, ternarised=False)

    dates = [tweet['date'] for tweet in recent]
    values = [tweet['sentiment'] for tweet in recent]

    vs.set_dates(dates)
    vs.set_values(values)
    vs.plot(average=AVERAGE)


if __name__ == '__main__':
    main() 