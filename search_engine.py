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
        self._doc_count = len(self._documents)
        # Watch out if query has words that never appear in documents
        self._inverted = self._process_inverted()
        self._idf = self._find_idf()

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

    def _find_idf(self):
        '''
        Finds the idf of each word in all of the documents
        Stores the term and a key and idf as a value in a dictionary
        Returns this dictionary
        '''
        idf = {}
        for word, count in self._inverted.items():
            idf[word] = self._calculate_idf(word)
        return idf

    def _find_inverted(self):
        inverted = {}
        for document in self._documents:
            for words in document.get_words_count().keys():
                for word in words:
                    if word in inverted:
                        inverted[word] = inverted[word] + 1
                    else:
                        inverted[word] = 1
        
        return inverted

    def _process_query(self, query):
        '''
        Takes a query as a string
        Normalizes all tokens in the query
        Returns a list of all tokens in the query
        '''
        que_list = query.split(' ')
        ret = []
        for word in que_list:
            ret.append(cse163_utils.normalize_token(word))

        return ret

        return [
            ['test_corpus/document2.txt', 'test_corpus/document3.txt'],
            ['test_corpus/document2.txt', 'test_corpus/document3.txt'],
            ['test_corpus/document2.txt', 'test_corpus/nsa.txt'],
            ['test_corpus/document2.txt', 'test_corpus/nsa.txt']][SearchEngine.test_count]
