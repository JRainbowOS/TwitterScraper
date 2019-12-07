from key_vault import (consumer_key,
                        consumer_secret,
                        access_token,
                        access_token_secret)

class Config():
    """
    Config file to keep keys secret
    """
    CONSUMER_KEY = consumer_key
    CONSUMER_SECRET = consumer_secret
    ACCESS_TOKEN = access_token
    ACCESS_TOKEN_SECRET = access_token_secret

    def __init__(self):
        self.consumer_key = Config.CONSUMER_KEY
        self.consumer_secret = Config.CONSUMER_SECRET
        self.access_token = Config.ACCESS_TOKEN
        self.access_token_secret = Config.ACCESS_TOKEN_SECRET


def main():
    cf = Config()
    print(cf.consumer_key)

if __name__ == '__main__':
    main()
