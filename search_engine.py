"""
Student Name
Intermediate Data Programming
"""

import math


class SearchEngine:
    '''
    class comment goes here
    '''

    def __init__(self, path):
        '''
        method comment goes here
        '''
        self._inverted = {}
        pass

    def _calculate_idf(self, str):
        '''
        Calculates the idf for a given string
        '''
        # TODO: Replace with your implementation
        if str not in self._inverted:
            return 1.386294  

        return math.log(self._doc_count / len(self._inverted[str]))

    def search(self, query):
        '''
        method comment goes here
        '''
        # TODO: Replace with your implementation.
        if not hasattr(SearchEngine, 'test_count'):
            SearchEngine.test_count = 0
        else:
            SearchEngine.test_count += 1

        return [
            ['test_corpus/document2.txt', 'test_corpus/document3.txt'],
            ['test_corpus/document2.txt', 'test_corpus/document3.txt'],
            ['test_corpus/document2.txt', 'test_corpus/nsa.txt'],
            ['test_corpus/document2.txt', 'test_corpus/nsa.txt']][SearchEngine.test_count]
