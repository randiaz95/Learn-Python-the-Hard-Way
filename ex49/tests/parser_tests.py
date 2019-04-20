from nose.tools import *
from ex49.parser import *


def test_sentence():
	print("Testing member variables on initialization.")
	sentenceInst = Sentence(("noun", "I"), 
							("verb", "want"), 
							("noun", "iced coffee"))
	assert_equals(sentenceInst.subject, 
				  "I")
	assert_equals(sentenceInst.verb, 
				  "want")
	assert_equals(sentenceInst.object, 
		          "iced coffee")

def test_peek():
	print("Testing Direction tuple in list.")
	assert_equals(peek([("direction", "north")]), 
				  "direction")

	print("Testing empty list")
	assert_equals(peek([]), 
				  None)

def test_match():
	print("Testing match with correct list and expectation.")
	assert_equals(match([("noun", "human"), ("noun", "alien")], "noun"),
				  ("noun", "human"))


	print("Testing with wrong expectation.")
	assert_equals(match([("noun", "human"), ("noun", "alien")], "verb"),
						None)

	print("Testing with empty list.")
	assert_equals(match([], "verb"), None)



def test_parse():
	print("Testing parse_verb with correct list.")
	assert_equals(parse_verb([("verb", "run")]), ("verb", "run"))

	print("Testing parse_verb with incorrect list.")
	assert_raises(ParserError, parse_verb, [("noun", "player")])


	print("Testing parse_object with correct list.")
	assert_equals(parse_object([("noun", "player")]), ("noun", "player"))

	print("Testing parse_object with incorrect list.")
	assert_raises(ParserError, parse_object, [("verb", "run")])


	print("Testing parse_subject with correct list.")
	assert_equals(parse_subject([("noun", "player")]), ("noun", "player"))

	print("Testing parse_subject with verb first, ( Assuming player if not noun ) ")
	assert_equals(parse_subject([("verb", "run")]), ("noun", "player"))

	print("Testing parse_subject with incorrect list.")
	assert_raises(ParserError, parse_subject, [("number", 1234)])


	print("Testing the parse function with a direction")
	assert_equals(parse("north"), ("direction", "north"))

	print("Testing the parse function with a verb")
	assert_equals(parse("go"), ("verb", "go"))
	
	print("Testing the parse function with a noun")
	assert_equals(parse("bear"), ("noun", "bear"))

	print("Testing the parse function with a number")
	assert_equals(parse("1"), ("number", 1))

	print("Testing the parse function with a stop word")
	assert_equals(parse("in"), ("stop", "in"))

	print("Testing the parse function with an error")
	assert_equals(parse("anything else"), ("error", "anything else"))


def test_scan():
	assert_equals(scan("bear go up"), [("noun", "bear"), ("verb", "go"), ("direction", "up")])




