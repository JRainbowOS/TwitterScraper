import tweepy
from key_vault import consumer_key, consumer_secret, access_token, access_token_secret

ACCOUNT_NAME = 'POTUS'
TWEET_COUNT = 20

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=ACCOUNT_NAME, count=TWEET_COUNT)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print(tweet.text)
   print('\n')