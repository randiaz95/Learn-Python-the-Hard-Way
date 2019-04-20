from nose.tools import *
import ex48.ex48 as lex

def test_directions():
	assert_equal(lex.scan("north"), [('direction', 'north')])
	result = lex.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						  ('direction', 'south'),
						  ('direction', 'east')])

def test_verbs():
	assert_equal(lex.scan("the"), [('stop', 'the')])
	result = lex.scan("the in of")
	assert_equal(result, [('stop', 'the'),
						  ('stop', 'in'),
						  ('stop', 'of')])

def test_nouns():
	assert_equal(lex.scan("bear"), [('noun', 'bear')])
	result = lex.scan("bear princess")
	assert_equal(result, [('noun', 'bear'),
						  ('noun', 'princess')])

def test_numbers():
	assert_equal(lex.scan("1234"), [('number', 1234)])
	result = lex.scan("bear IAS princess")
	assert_equal(result, [('noun', 'bear'),
						  ('error', 'IAS'),
						  ('noun', 'princess')])
	