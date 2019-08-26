from os import environ

'''
Local Settings for a heroku_ebooks account.
'''

# Configuration for Twitter API
ENABLE_TWITTER_SOURCES = False # Fetch twitter statuses as source
ENABLE_TWITTER_POSTING = True # Tweet resulting status?
MY_CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY') #Your Twitter API Consumer Key set in Heroku config
MY_CONSUMER_SECRET = environ.get('TWITTER_CONSUMER_SECRET') #Your Consumer Secret Key set in Heroku config
MY_ACCESS_TOKEN_KEY = environ.get('TWITTER_ACCESS_TOKEN_KEY') #Your Twitter API Access Token Key set in Heroku config
MY_ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_SECRET') #Your Access Token Secret set in Heroku config

ODDS = environ.get('ORDER')  # How often do you want this to run? 1/8 times?
ORDER = 1  # How closely do you want this to hew to sensical? 2 is low and 4 is high.

DEBUG = False  # Set this to False to start Tweeting live
TWEET_ACCOUNT = "lefttube_ebooks"  # The name of the account you're tweeting to.
