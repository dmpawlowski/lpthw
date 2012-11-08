from nose.tools import *
from ex48.parser import *

# testing logic: given, when, then
 
def test_words():
    return [('noun', 'princess')]

def verb_words():
    return [('verb', 'go')]
    
def direction_words():
    return[('direction', 'north')]
    
def sentence_list():
    return[('verb', 'go'), ('direction', 'north')]
    
def empty_words():
    return []

def test_peek_returns_word_type():
    result = peek(test_words()) #given, when
    assert_equal(result, 'noun') #then
    
def test_peek_returns_none_when_not_passed_word_list():
    result = peek(empty_words())
    assert_equal(result, None)
    
def test_match_returns_word_type_tuple():
    result = match(test_words(), 'noun')
    assert_equal(result, ('noun', 'princess'))
    
def test_match_returns_none_when_not_matching():
    result = match(test_words(), 'verb')
    assert_equal(result, None)

def test_match_returns_none_when_not_passed_word_list():
    result = match(empty_words(), 'verb')
    assert_equal(result, None)
    
def test_skip_word_type_matches():
    result = skip(test_words(), 'noun')
    assert_equal(result, None)
    
def test_skip_word_type_does_not_match():
    result = skip(test_words(), 'verb')
    assert_equal(result, None)

def test_parse_verb_with_verb():
    result = parse_verb(verb_words())
    assert_equal(result, ('verb', 'go'))

#def test_parse_verb_with_non_verb():
#    result = parse_verb(test_words())
#    assert_equal(None)
  
def test_parse_object_with_noun():
    result = parse_object(test_words())
    assert_equal(result, ('noun', 'princess'))
    
def test_parse_object_with_direction():
    result = parse_object(direction_words())
    assert_equal(result, ('direction', 'north'))
    
# def test_parse_object_with_empty():

def test_parse_subject():
    result = parse_subject(sentence_list(), ('noun', 'princess'))
    assert_equal(result.subject, 'princess')
    assert_equal(result.verb, 'go')
    assert_equal(result.object, 'north')

def test_parse_sentence_with_noun():
    sentence_list = [('stop', 'of'), ('verb', 'go'), ('direction', 'north')]
    result = parse_sentence(sentence_list)
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'go')
    assert_equal(result.object, 'north')
        
# def test_parse_sentence_with_empty():        

