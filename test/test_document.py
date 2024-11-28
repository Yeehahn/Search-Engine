"""
CSE 163: HW5 Part 0 - Subset of Tests
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from document import Document as DocumentStudent


class TestPart0(unittest.TestCase):
    """Tests for hw5, part 0"""

    def setUp(self):
        self._test_file = 'test_corpus/document1.txt'
        self._test_file_long = 'test_corpus/nsa.txt'
        self._student = DocumentStudent(self._test_file)
        self._student_long = DocumentStudent(self._test_file_long)

    def test_p0_term_freq_zero_return_long(self):
        """
        #name([Behavior: Edge Case] D2: Testing document term_frequency on long file, returns zero)
        """
        # msg = 'Testing compute_frequencies on nsa.txt, zero return'
        sol = self._student_long.term_frequency('asdfasdf')
        self.assertTrue(sol == 0)

    def test_p0_term_freq_long(self):
        """
        #name([Behavior: Edge Case] D3: Testing document term_frequency nsa.txt, ignore cases and punctuation)
        """
        msg = 'Testing compute_frequencies on nsa.txt'
        term = 'coLleCtion...'
        sol = self._student_long.term_frequency(term)
        ans = 0.00871459
        self.assertAlmostEqual(sol, ans, delta=0.001, msg=msg)

    def test_get_words_returns_list(self):
        """
        #name([Behavior: Common Case] D5: Tests whether get_words returns a list)
        """
        words = self._student.get_words()
        self.assertTrue(isinstance(words, list))