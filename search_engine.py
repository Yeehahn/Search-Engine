"""
Yeehahn Wang-Liu
Intermediate Data Programming
"""

import math
import cse163_utils
import os
from document import Document


class SearchEngine:
    '''
    class comment goes here
    '''

    def __init__(self, path):
        '''
        method comment goes here
        '''
        self._documents = self._create_documents(path)
        self._inverted = {}
        self._idf = {}
        self._query = set()

    def _create_documents(self, path):
        file_paths = [os.path.join(path, f) for f in os.listdir(path)]
        documents = []
        for file_path in file_paths:
            documents.append(Document(file_path))

        return documents

    def _calculate_idf(self, term):
        '''
        Calculates the idf for a given string
        '''

        return math.log(self._doc_count / len(self._inverted[term]))

    def search(self, query):
        '''
        method comment goes here
        '''
        self._query = self._process_query(query)
        self._inverted = self._process_inverted()
        self._idf = _find_idf()

    def _find_idf(self):
        for word in self._query:
            self._idf[word] = self._calculate_idf(word)

    def _process_inverted(self):
        for word in self._query:
            self._inverted[word] = 0

        for document in self._documents:
            for word in self._query:
                if word in document.get_words():
                    self._inverted[word] = self._inverted[word] + 1
        return self._inverted

    def _process_query(self, query):
        que = query.split(' ')
        for word in que:
            self._query.add(cse163_utils.normalize_token(word))
        
        return self._query

        return [
            ['test_corpus/document2.txt', 'test_corpus/document3.txt'],
            ['test_corpus/document2.txt', 'test_corpus/document3.txt'],
            ['test_corpus/document2.txt', 'test_corpus/nsa.txt'],
            ['test_corpus/document2.txt', 'test_corpus/nsa.txt']][SearchEngine.test_count]
