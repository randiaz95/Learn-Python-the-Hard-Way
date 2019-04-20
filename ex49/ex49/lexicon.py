
def parse(word):
	word_type = "error"

	if word in ["north", "south", "east"]:
		word_type = "direction"
	elif word in ["go", "kill", "eat"]:
		word_type = "verb"
	elif word in ["bear", "princess"]:
		word_type = "noun"
	elif word[0] in "1234567890":
		word_type = "number"
		for i in word:
			if not i in "1234567890":
				word_type=""

		if word_type == "number":
			word = int(word)

	elif word in ["the", "as", "in", "of"]:
		word_type = "stop"
	else:
		word_type = "error"

	return (word_type, word)


def scan(text):
	return [parse(word) for word in text.split()]

