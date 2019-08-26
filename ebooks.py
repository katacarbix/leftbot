import re
import twitter
import markov2 as markov
import HTMLParser
from local_settings import *
from corpus import *

def connect():
	return twitter.Api(consumer_key=MY_CONSUMER_KEY,
					   consumer_secret=MY_CONSUMER_SECRET,
					   access_token_key=MY_ACCESS_TOKEN_KEY,
					   access_token_secret=MY_ACCESS_TOKEN_SECRET,
					   tweet_mode='extended')

def format(text):
	text = re.sub('\s+', ' ', text)  # collaspse consecutive whitespace to single spaces.
	text.lstrip().rstrip()
	text = HTMLParser.HTMLParser().unescape(text) # unescape html entities, such as "&amp;"
	return text

if __name__ == "__main__":
	order = ORDER
	source_statuses = list(corpus)

	if len(source_statuses) == 0:
		print("No statuses found!")
		sys.exit()

	mine = markov.MarkovChainer(order)
	for text in source_statuses:
		text = format(text)
		mine.add_text(text)

	ebook_status = None
	while ebook_status == None:
		ebook_status = mine.generate_sentence()

	status = format(ebook_status)
	print(status)

	if not DEBUG and ENABLE_TWITTER_POSTING:
		api = connect()
		status = api.PostUpdate(status)
