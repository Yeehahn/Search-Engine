"""
Yeehahn Wang-Liu
Intermediate Data Programming
"""
import cse163_utils


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
        self._words = self.get_words()
        self._words_count = self._find_words_count(self._words)

    def _find_words_count(self, words):
        words_count = {}
        for word in words:
            if word in words_count:
                words_count[word] = words_count[word] + 1
            else:
                words_count[word] = 1

        return words_count

    def find_words(self):
        '''
        Stores each normalized word in the file given by the path
        as an element in a list.
        Returns this list
        '''
        words = []
        with open(self._path) as file:
            lines = file.readlines()
            for line in lines:
                for word in line:
                    words.append(cse163_utils.normalize_token(word))

        return words

    def get_words(self):
        return self._words

    def get_words_count(self):
        return self._words_count

    def term_frequency(self, term):
        '''
        Takes a term and returns the term frequency
        Term frequency is the number of times a term occurrs in a document
        divided by the number of words in the document
        '''
        return self._words_count[term] / len(self._words)


