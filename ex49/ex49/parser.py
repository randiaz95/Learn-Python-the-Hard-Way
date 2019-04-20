
class Parser(Exception):
	pass

class Sentence:
	def __init__(self, subject, verb, obj):
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]

def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)

		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None

def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)

def parse_verb(word_list):
	skip(word_list, "stop")

	if peek(word_list) == "verb":
		return match(word_list, "verb")
	else:
		raise ParserError("Expected a verb next.")


def parse_object(word_list):
	skip(word_list, "stop")
	next_word = peek(word_list)

	if next_word == "noun":
		return match(word_list, "noun")
	elif next_word == "direction":
		return match(word_list, "direction")
	else:
		raise ParserError("Expected an object next.")

def parse_subject(word_list):
	skip(word_list, "stop")
	next_word = peek(word_list)

	if next_word == "noun":
		return match(word_list, "noun")
	elif next_word == "verb":
		return ("noun", "player")
	else:
		raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
	subject = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subject, verb, obj)


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

