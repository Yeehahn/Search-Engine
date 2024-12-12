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
    This object is given a path and creates a search engine
    for a corpus of documents given by the path
    Can search for documents by inputting a search
    and the search engine will return a sorted list of relevant documents
    '''

    def __init__(self, path):
        '''
        Creates an instance of a search engine for a corpus of text given by a path
        Stores documents in inverse index and pre-processes term frequencies 
        and inverse document frequencies
        '''
        doc_count, documents = self._create_documents(path)
        self._documents = documents
        self._doc_count = doc_count
        # Watch out if query has words that never appear in documents
        self._idf = self._find_idf(self._documents)
        self._path = path

    def _create_documents(self, path):
        '''
        Given a path
        Creates a list of documents for each txt file in given path
        '''
        file_paths = [os.path.join(path, f) for f in os.listdir(path)]
        doc_count = len(file_paths)
        documents = {}
        for file_path in file_paths:
            document = Document(file_path)
            for word in document.get_words():
                if word in documents.keys():
                    documents[word].add(document)
                else:
                    documents[word] = {document}

        return (doc_count, documents)

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

    def _assign_tf_idf(self, query, relevant_documents):
        '''
        Given the query and all relevant documents for that query
        Calculates the tf-idf for each relevant document
        Stores the document as a key and the corresponding tf-idf as a value in a dictionary
        Returns the dictionary
        '''
        documents_tf_idf = {}
        for document in relevant_documents:
            tf_idf = 0
            for word in query:
                tf_idf += document.term_frequency(word) * self._inverse_document_frequency(word)

            if tf_idf > 0:
                documents_tf_idf[document.get_path()] = tf_idf

        return documents_tf_idf

    def _find_relevant_documents(self, query):
        '''
        Given a query it finds all documents that contain words in query
        Returns this list of documents
        '''
        relevant_docs = []
        for word in query:
            if word in self._documents.keys():
                documents_contain_word = self._documents[word]
                for document in documents_contain_word:
                    if document not in relevant_docs:
                        relevant_docs.append(document)
        return relevant_docs

    def search(self, query):
        '''
        Given a query returns a list of relevant document paths
        Sorted by relevancy
        '''
        query = self._process_query(query)
        # What happens if empty?
        relevant_docs = self._find_relevant_documents(query)
        documents_tf_idf = self._assign_tf_idf(query, relevant_docs)
        sorted_docs = sorted(documents_tf_idf.items(), key=lambda x: x[1], reverse=True)

        ret_docs = []
        for i in range(len(sorted_docs)):
            ret_docs.append(sorted_docs[i][0])
        return ret_docs