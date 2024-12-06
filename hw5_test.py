"""
Yeehahn Wang-Liu
Intermediate Data Programming
"""

# The tests you create will be graded

from cse163_utils import assert_equals
from cse163_utils import normalize_paths

# from document import Document
from search_engine import SearchEngine
from document import Document

# This file is left blank for you to fill in with your tests!


def test_search():
    '''
    This method is an Example Test showing how to normalize paths.
    Do not include this test as one of your own!
    '''
    engine = SearchEngine('directory')
    expected = ['directory/doc1.txt', 'directory/doc2.txt']
    actual = engine.search('my query')
    # Please normalize the paths!!
    expected = normalize_paths(expected)
    actual = normalize_paths(actual)
    assert_equals(expected, actual)


def test_create_documents():
    engine = SearchEngine('test_corpus')
    expected = [Document('test_corpus/document1.txt')._words, 
                Document('test_corpus/document2.txt')._words,
                Document('test_corpus/document3.txt')._words,
                Document('test_corpus/nsa.txt')._words]
    actual = [document._words for document in engine._documents]
    assert_equals(expected, actual)


def test_idf():
    '''
    Tests if SearchEngine properly finds the idf value
    for each word in the given query
    '''


def main():
    test_create_documents()


if __name__ == '__main__':
    main()