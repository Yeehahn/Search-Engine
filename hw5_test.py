"""
Student Name
Intermediate Data Programming
"""

# The tests you create will be graded

from cse163_utils import assert_equals
from cse163_utils import normalize_paths

# from document import Document
from search_engine import SearchEngine


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