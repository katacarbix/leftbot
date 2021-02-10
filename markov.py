import random

kword_bgn = "__BEGIN__"
kword_end = "__END__"

class Markov:
	def __init__(self, corpus=[]):
		self.tokens = {}
		self.ingest(corpus)

	def ingest(self, corpus):
		prev = ""
		next = ""

		for line in corpus:
			words = line.split(' ')
			words_len = len(words)
			i = 0

			while i <= words_len:
				if i == 0:
					prev = kword_bgn
					next = words[i]
				elif i == words_len:
					prev = words[i-1]
					next = kword_end
				else:
					prev = words[i-1]
					next = words[i]

				if prev in self.tokens:
					if next in self.tokens[prev]:
						self.tokens[prev][next] += 1
					else:
						self.tokens[prev][next] = 1
				else:
					self.tokens[prev] = {}
					self.tokens[prev][next] = 1

				i += 1

	def generate(self):
		chain = [kword_bgn]
		i = 0

		while chain[-1] != kword_end:
			choices = []
			key = chain[i]

			for k,v in self.tokens[key].items():
				for j in range(v):
					choices.append(k)

			word = random.choice(choices)
			chain.append(word)

			i += 1

		return chain

	def make_sentence(self):
		chain = self.generate()
		return ' '.join(chain[1:-1])

	def make_short_sentence(self, length):
		while True:
			sentence = self.make_sentence()
			if len(sentence) <= length:
				return sentence

if __name__ == "__main__":
	with open("data/corpus.txt") as f:
		corpus = f.read().splitlines()
		m = Markov(corpus)
		print(m.make_short_sentence(280))
