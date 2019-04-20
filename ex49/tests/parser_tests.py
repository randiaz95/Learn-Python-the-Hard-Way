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
				  ("noun", "human")


	print("Testing with wrong expectation.")
	assert_equals(match([("noun", "human"), ("noun", "alien")], "verb"),
						None)

	print("Testing with empty list.")
	assert_equals(match([], "verb"), None)