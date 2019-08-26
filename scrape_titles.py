import json
import urllib

API_KEY = 'AIzaSyDDPKNMshWjooLm1YLBUufIa-lSLKG06bY'

channels_path = 'channels.txt'
corpus_path = 'corpus.txt'
corpus = []

with open(channels_path, 'r') as f:
	for line in f:
		data = json.loads(urllib.urlopen('https://www.googleapis.com/youtube/v3/search?key='+API_KEY+'&channelId='+(line.rstrip())+'&part=snippet&maxResults=50&order=date&safeSearch=none').read())
		try:
			for item in data['items']:
				print item['snippet']['title']
				corpus.append(item['snippet']['title'])
		except:
			print data

f.close()

of = open(corpus_path, 'w')
of.write(str(corpus))
of.close()