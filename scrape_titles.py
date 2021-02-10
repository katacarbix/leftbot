import json
import html
import re
import requests
from settings import GITLAB_API_KEY

corpus_file = "data/corpus.txt"

def format(text):
	return re.sub('\s+', ' ', html.unescape(text)).lstrip().rstrip()

def main():
	response = requests.get(
		'https://gitlab.com/api/v4/projects/19386663/repository/files/data%2fvideos.json/raw',
		params={
			'ref': 'master',
			'private_token': GITLAB_API_KEY
		},
		timeout=60
	)
	if response.status_code != requests.codes.ok:
		print(f'Error retrieving video list (code {response.status_code})')
		print(response.headers)
		return

	data = json.loads(response.text)

	corpus = set()
	with open(corpus_file) as f:
		for line in f.readlines():
			corpus.add(line.rstrip())

	for video in data:
		line = format(video['name'])
		corpus.add(line)

	with open(corpus_file, 'w') as f:
		f.write('\n'.join(corpus))

if __name__ == '__main__':
	main()
