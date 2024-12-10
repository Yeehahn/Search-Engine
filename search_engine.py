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

        self._doc_count = len(self._documents.values())
        # Watch out if query has words that never appear in documents
        self._idf = self._find_idf(self._documents)
        self._path = path

    def _create_documents(self, path):
        '''
        Given a path
        Creates a list of documents for each txt file in given path
        '''
        file_paths = [os.path.join(path, f) for f in os.listdir(path)]
        documents = {}
        for file_path in file_paths:
            document = Document(file_path)
            for word in document.get_words():
                if word in documents.keys():
                    documents[word].add(document)
                else:
                    documents[word] = {document}

        return documents

    def _calculate_idf(self, term):
        '''
        Calculates the idf for a given string
        '''
        return math.log(self._doc_count / len(self._documents[term]))

    def _find_idf(self, documents):
        '''
        Finds the idf of each word in all of the documents
        Stores the term and a key and idf as a value in a dictionary
        Returns this dictionary
        '''
        idf = {}
        for word in documents.keys():
            idf[word] = self._calculate_idf(word)
        return idf

    def _inverse_document_frequency(self, term):
        '''
        Returns the inverse document frequency value of a given term
        returns 0 if the term is not in any of the documents
        '''
        if term in self._idf.keys():
            return self._idf[term]
        else:
            return 0

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

    def _assign_td_idf(self, query, relevant_documents):
        documents_td_idf = {}
        for document in relevant_documents:
            td_idf = 0
            for word in query:
                td_idf += document.term_frequency(word) * self._inverse_document_frequency(word)

            if td_idf > 0:
                documents_td_idf[document] = td_idf

        return documents_td_idf

    def _find_relevant_documents(self, query):
        relevant_docs = set()
        for word in query:
            documents_contain_word = self._documents[word]
            for document in documents_contain_word:
                relevant_docs.add(document)

        return relevant_docs

    def search(self, query):
        query = self._process_query(query)
        # What happens if empty?
        relevant_docs = self._find_relevant_documents(query)
        print(relevant_docs)
        documents_td_idf = self._assign_td_idf(query, relevant_docs)
        sorted_docs = sorted(documents_td_idf.items(), key=lambda x: x[1])
        for i in range(0, min(10, len(sorted_docs))):
            print(f'{i}. {sorted_docs[i][0].get_path()}')