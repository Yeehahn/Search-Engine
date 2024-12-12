"""
Yeehahn Wang-Liu
Intermediate Data Programming
"""

# The tests you create will be graded

from cse163_utils import assert_equals

# from document import Document
from search_engine import SearchEngine
from document import Document
import math
# This file is left blank for you to fill in with your tests!


def test_create_documents():
    engine = SearchEngine('test_corpus')
    expected = {' '.join(Document('test_corpus/document1.txt')._words), 
                ' '.join(Document('test_corpus/document2.txt')._words),
                ' '.join(Document('test_corpus/document3.txt')._words),
                ' '.join(Document('test_corpus/nsa.txt')._words)}
    actual = {' '.join(document._words) for set_docs in engine._documents.values() for document in set_docs}
    assert_equals(expected, actual)


def test_document_frequnecy():
    '''
    Tests if SearchEnginge properly finds the count
    '''
    engine = SearchEngine('test_corpus')
    expected_I = 3
    expected_love = 1
    actual_I = len(engine._documents['i'])
    actual_love = len(engine._documents['love'])
    assert_equals(expected_I, actual_I)
    assert_equals(expected_love, actual_love)


def test_idf():
    '''
    Tests if SearchEngine properly finds the idf value
    for each word in the given query
    '''
    engine = SearchEngine('test_corpus')
    expected_I = math.log(4 / 3)
    expected_love = math.log(4 / 1)
    actual_I = engine._idf['i']
    actual_love = engine._idf['love']
    assert_equals(expected_I, actual_I)
    assert_equals(expected_love, actual_love)


def test_find_relevant_documents():
    engine = SearchEngine('test_corpus')
    expected = sorted([Document('test_corpus/document2.txt')._words,
                       Document('test_corpus/nsa.txt')._words,
                       Document('test_corpus/document3.txt')._words])
    rel_docs = engine._find_relevant_documents(['systems', 'puppies'])
    actual = sorted([docs._words for docs in rel_docs])
    assert_equals(expected, actual)


def test_assign_tf_idf():
    engine = SearchEngine('test_corpus')
    query = ['systems', 'puppies']
    relevant_documents = engine._find_relevant_documents(query)
    actual = engine._assign_tf_idf(query, relevant_documents)
    expected = {'test_corpus/document2.txt': 0.17328679513998632, 
                'test_corpus/nsa.txt': 0.003040119212982216, 
                'test_corpus/document3.txt': 0.2772588722239781}
    assert_equals(actual, expected)


def test_search():
    engine = SearchEngine('test_corpus')  
    actual = engine.search('systems puppies')
    expected = ['test_corpus/document3.txt', 'test_corpus/document2.txt', 'test_corpus/nsa.txt']
    assert_equals(expected, actual)


def main():
    test_create_documents()
    test_document_frequnecy()
    test_idf()
    test_find_relevant_documents()
    test_assign_tf_idf()
    test_search()


if __name__ == '__main__':
    main()