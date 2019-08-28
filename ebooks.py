import re
import twitter
import markovify
import textdistance
from local_settings import *

def connect():
	return twitter.Api(consumer_key=MY_CONSUMER_KEY,
					   consumer_secret=MY_CONSUMER_SECRET,
					   access_token_key=MY_ACCESS_TOKEN_KEY,
					   access_token_secret=MY_ACCESS_TOKEN_SECRET,
					   tweet_mode='extended')

def tweet(body):
	if ENABLE_TWITTER_POSTING:
		api = connect()
		return api.PostUpdate(body)
	return None

if __name__ == "__main__":
	with open("data/corpus.txt") as f:
		corpus = f.read().splitlines()

	model = markovify.Text(corpus, retain_original=False, state_size=ORDER)

	status = None
	while status == None or True in [textdistance.lcsstr.normalized_similarity(status, x) >= 0.6 for x in corpus]:
		status = model.make_short_sentence(280)

	print(status)
	tweet(status)
