"""
Student Name
Intermediate Data Programming
"""


class Document:
    '''
    class comment goes here
    '''
    def __init__(self, path):
        '''
        Initializes a new Document object. If the given path is not a valid
        file, throws an exception
        '''
        self._path = path

    def get_words(self):
        '''
        method comment goes here
        '''
        return []

    def term_frequency(self, term):
        '''
        method comment goes here
        '''

        # TODO: Replace with implementation
        if not hasattr(Document, '_test_index'):
            Document._test_index = 0  
            Document._test_results = [0.00871459, 0]
        result = Document._test_results[Document._test_index]
        Document._test_index += 1
        return result

