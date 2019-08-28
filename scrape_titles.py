import json
import html
from urllib.request import urlopen
from local_settings import GOOGLE_API_KEY

channels_path = "data/channels.txt"
corpus_path = "data/corpus.txt"

def format(text):
	text = re.sub('\s+', ' ', text)  # collaspse consecutive whitespace to single spaces.
	text = html.unescape(text)
	text.lstrip().rstrip()
	return text

with open(channels_path, 'r') as f1:
	with open(corpus_path, 'a') as f2:
		for line in f1:
			url = "https://www.googleapis.com/youtube/v3/search?key="+GOOGLE_API_KEY+"&channelId="+(line.lstrip().rstrip())+"&part=snippet&maxResults=50&order=date&safeSearch=none"
			data = json.loads(urlopen(url).read())
			try:
				for item in data["items"]:
					title = format(item["snippet"]["title"])
					f2.write(title + "\n")
			except:
				print(data)
				break

f1.close()
f2.close()
