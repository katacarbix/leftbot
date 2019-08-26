import markovify

class MarkovChainer(object):
	def __init__(self, order):
		self.text = []
		self.order = order

	# pass a string to add it to the markov lists.
	def add_text(self, text):
		self.text.append(str(text))

	# Generate the goofy sentences that become your tweet.
	def generate_sentence(self):
		self.model = markovify.Text(self.text, state_size=self.order)
		return self.model.make_short_sentence(280)


if __name__ == "__main__":
	print("Try running ebooks.py first")
