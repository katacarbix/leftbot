from os import environ

# Configuration for Twitter API
ENABLE_TWITTER_POSTING = True # Tweet resulting status?
MY_CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY') # Your Twitter API Consumer Key set in Heroku config
MY_CONSUMER_SECRET = environ.get('TWITTER_CONSUMER_SECRET') # Your Consumer Secret Key set in Heroku config
MY_ACCESS_TOKEN_KEY = environ.get('TWITTER_ACCESS_TOKEN_KEY') # Your Twitter API Access Token Key set in Heroku config
MY_ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_SECRET') # Your Access Token Secret set in Heroku config

GITLAB_API_KEY = environ.get('GITLAB_API_KEY') # Google/Youtube API key for scraping titles
