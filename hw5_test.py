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
    '''
    Tests the create documents method
    '''
    engine = SearchEngine('test_corpus')
    expected = {' '.join(Document('test_corpus/document1.txt')._words), 
                ' '.join(Document('test_corpus/document2.txt')._words),
                ' '.join(Document('test_corpus/document3.txt')._words),
                ' '.join(Document('test_corpus/nsa.txt')._words)}
    actual = {' '.join(document._words) for set_docs in engine._documents.values() for document in set_docs}
    assert_equals(expected, actual)


def test_document_frequnecy():
    '''
    Tests if SearchEngine properly finds the count
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
    '''
    Tests if the search engine can properly find relevant documents
    given a query
    '''
    engine = SearchEngine('test_corpus')
    expected = sorted([Document('test_corpus/document2.txt')._words,
                       Document('test_corpus/nsa.txt')._words,
                       Document('test_corpus/document3.txt')._words])
    rel_docs = engine._find_relevant_documents(['systems', 'puppies'])
    actual = sorted([docs._words for docs in rel_docs])
    assert_equals(expected, actual)


def test_assign_tf_idf():
    '''
    Tests if SearchEngine can properly assign tf-idf values for documents
    given a query
    '''
    engine = SearchEngine('test_corpus')
    query = ['systems', 'puppies']
    relevant_documents = engine._find_relevant_documents(query)
    actual = engine._assign_tf_idf(query, relevant_documents)
    expected = {'test_corpus/document2.txt': 0.17328679513998632, 
                'test_corpus/nsa.txt': 0.003040119212982216, 
                'test_corpus/document3.txt': 0.2772588722239781}
    assert_equals(actual, expected)


def test_search():
    '''
    Tests basic multi-word search
    '''
    engine = SearchEngine('test_corpus')  
    actual = engine.search('systems puppies')
    expected = ['test_corpus/document3.txt', 'test_corpus/document2.txt', 'test_corpus/nsa.txt']
    assert_equals(expected, actual)


def test_search_bad_search():
    '''
    Tests edge-case where search has no valid terms
    '''
    engine = SearchEngine('test_corpus')  
    actual = engine.search('rahasdfa;lkh')
    expected = []
    assert_equals(expected, actual)


def test_multi_word_bad_search():
    '''
    Tests edge-case where bad terms are in an actual search
    '''
    engine = SearchEngine('test_corpus')  
    actual = engine.search('rahasdfa;lkh love gaasdf;alhasdfhb puppies')
    expected = ['test_corpus/document1.txt', 'test_corpus/document3.txt']
    assert_equals(expected, actual)


def test_empty_search():
    '''
    Tests empty search
    '''
    engine = SearchEngine('test_corpus')  
    actual = engine.search('')
    expected = []
    assert_equals(expected, actual)


def test_non_normal_search():
    '''
    Tests search where terms are don't follow the normalized conventions
    '''
    engine = SearchEngine('test_corpus')  
    actual = engine.search('sYsTems     puPpIes....')
    expected = ['test_corpus/document3.txt', 'test_corpus/document2.txt', 'test_corpus/nsa.txt']
    assert_equals(expected, actual)


def test_find_words():
    '''
    Tests Document class's find_words method
    '''
    doc = Document('test_corpus/document1.txt')
    actual = doc._find_words()
    expected = ['i', 'love', 'bruno']
    assert_equals(expected, actual)


def test_find_words_empty():
    '''
    Tests edge-case where document is empty
    '''
    doc = Document('test_corpus_2/empty.txt')
    actual = doc._find_words()
    expected = []
    assert_equals(expected, actual)


def test_term_frequency():
    '''
    Tests Document term frequency method
    '''
    doc = Document('test_corpus/document1.txt')
    actual = doc.term_frequency('i')
    expected = 1 / 3
    assert_equals(expected, actual)


def test_term_frequency_bad_search():
    '''
    Tests term frequency but given term is not a term in document
    '''
    doc = Document('test_corpus/document1.txt')
    actual = doc.term_frequency('gabadasdf')
    expected = 0
    assert_equals(expected, actual)


def test_term_frequency_empty():
    '''
    Tests term frequency given an empty search
    '''
    doc = Document('test_corpus/document1.txt')
    actual = doc.term_frequency('')
    expected = 0
    assert_equals(expected, actual)


def test_find_words_count():
    '''
    Tests find_words_count method
    '''
    doc = Document('test_corpus/document3.txt')
    actual = doc._find_words_count(doc._words)
    expected = {'i': 2, 'like': 2, 'puppies': 1}
    assert_equals(expected, actual)


def test_find_words_count_2():
    '''
    Tests find_words_count method
    '''
    doc = Document('test_corpus/document1.txt')
    actual = doc._find_words_count(doc._words)
    expected = {'i': 1, 'love': 1, 'bruno': 1}
    assert_equals(expected, actual)


def test_find_words_a():
    '''
    Tests find_words method
    '''
    doc = Document('test_corpus_2/a.txt')
    actual = sorted(doc.get_words())
    expected = sorted(['a', 'ability', 'as'])
    assert_equals(expected, actual)


def test_document():
    '''
    Tests methods in the Document class
    '''
    test_find_words()
    test_find_words_empty()
    test_term_frequency()
    test_term_frequency_bad_search()
    test_term_frequency_empty()
    test_find_words_count()
    test_find_words_count_2()
    test_find_words_a()


def test_search_engine():
    '''
    Tests methods in the SearchEngine class
    '''
    test_create_documents()
    test_document_frequnecy()
    test_idf()
    test_find_relevant_documents()
    test_assign_tf_idf()
    test_search()
    test_search_bad_search()
    test_empty_search()
    test_multi_word_bad_search()
    test_non_normal_search()


def main():
    test_search_engine()
    test_document()


if __name__ == '__main__':
    main()