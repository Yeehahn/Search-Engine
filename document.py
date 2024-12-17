"""
Yeehahn Wang-Liu
Intermediate Data Programming
"""
import cse163_utils
import os


class Document:
    '''
    Document stores information of a text file
    Stores words in a list
    Stores the number of times a word ocurrs in a document as a dictionary
    Stores the term_frequency value of each word
    Users can find term frequencies
    '''
    def __init__(self, path):
        '''
        Initializes a new Document object. If the given path is not a valid
        file, throws an exception
        '''
        self._path = cse163_utils.normalize_paths(path)

        if not os.path.isfile(self._path):
            raise FileNotFoundError("Non-valid path")

        self._words = self._find_words()
        self._words_count = self._find_words_count(self._words)
        self._term_frequency = self._process_term_frequency(self._words_count)

    def _find_words_count(self, words):
        '''
        Takes a list of words
        Counts how many times each word occurrs in the list
        Returns the counts of words as a dictionary where word is key and count is value
        '''
        words_count = {}
        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

        return words_count

    def _find_words(self):
        '''
        Stores each normalized word in the file given by the path
        as an element in a list.
        Returns this list
        '''
        words = []
        with open(self._path) as file:
            words_in_file = file.read().split()
            for word in words_in_file:
                words.append(cse163_utils.normalize_token(word))

        return words

    def _process_term_frequency(self, words_count):
        '''
        Takes the dictionary of the counts of all words in the document
        Calculates the term frequency of each term in the document
        Returns a dictionary of the value of the term frequency for each term
        '''
        tot_words = len(self._words)
        tf = {}
        for word, count in words_count.items():
            tf[word] = count / tot_words

        return tf

    def get_words(self):
        '''
        Returns the words in document
        '''
        return list(set(self._words))

    def get_words_count(self):
        '''
        Returns the dictionary of words and count of words
        '''
        return self._words_count

    def get_path(self):
        '''
        Returns the path to the document
        '''
        return self._path

    def term_frequency(self, term):
        '''
        Takes a term that was normalized and returns the term frequency
        Term frequency is the number of times a term occurrs in a document
        divided by the number of words in the document
        If the term never appears in the document returns 0
        '''
        term = cse163_utils.normalize_token(term)
        if term in self._term_frequency.keys():
            return self._term_frequency[term]
        else:
            return 0


