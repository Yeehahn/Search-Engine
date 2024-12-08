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
        self._document_frequency = self._find_document_frequency(self._documents)
        self._idf = self._find_idf()

    def _create_documents(self, path):
        '''
        Given a path
        Creates a list of documents for each txt file in given path
        '''
        file_paths = [os.path.join(path, f) for f in os.listdir(path)]
        documents = []
        for file_path in file_paths:
            documents.append(Document(file_path))

        return documents

    def _calculate_idf(self, term):
        '''
        Calculates the idf for a given string
        '''
        return math.log(self._doc_count / self._document_frequency[term])

    def _find_idf(self):
        '''
        Finds the idf of each word in all of the documents
        Stores the term and a key and idf as a value in a dictionary
        Returns this dictionary
        '''
        idf = {}
        for word in self._document_frequency.keys():
            idf[word] = self._calculate_idf(word)
        return idf

    def _find_document_frequency(self, documents):
        '''
        Takes a list of documents
        Counts the number of documents that contain each term
        Returns a dictionary where keys are terms and values are the count
        '''
        document_frequency = {}
        for document in documents:
            for word in document.get_words_count().keys():
                if word in document_frequency:
                    document_frequency[word] = document_frequency[word] + 1
                else:
                    document_frequency[word] = 1
        return document_frequency

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

    def _
    
    def search(self, query):
        query = self._process_query(query)
        