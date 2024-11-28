"""
CSE 163: HW5 Part 0 - Subset of Tests
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from search_engine import SearchEngine as SearchStudent


class TestPart1(unittest.TestCase):
    """Tests for hw5"""

    def setUp(self):
        self._test_dir = 'test_corpus'
        self._student = SearchStudent(self._test_dir)

    # --- PART 1 ---
    def test_p1_search_single_word_ignore_order(self):
        """
        #name([Behavior: Common Case] Testing search_engine single word search on directory, ignores order)
        """
        msg = "Testing search_engine single word search for 'like'. \
               Ignores order of returned list."
        result = sorted(self._student.search('like'))
        expected = ['test_corpus/document2.txt', 'test_corpus/document3.txt']
        self.assertEqual(result, expected, msg)

    def test_p1_calculate_idf(self):
        """
        #name([Behavior: Edge Case] SE2: Testing _calculate_idf on directory)
        """
        msg = 'IDF not correct for bruno'
        result = self._student._calculate_idf('bruno')
        expected = 1.386294
        self.assertAlmostEqual(expected, result, delta=0.001, msg=msg)

    def test_p1_search_single_word_ignore_order_long(self):
        """
        #name([Behavior: Common Case] SE3: Search_engine single word search, ignores order)
        """
        msg = 'Testing search_engine search ignores order'
        result = sorted(self._student.search('like'))
        expected = ['test_corpus/document2.txt', 'test_corpus/document3.txt']
        self.assertEqual(expected, result, msg)

    # PART 2:
    def test_p2_search_multi_word_hard_spec(self):
        """
        #name([Behavior: Common Case] SE8: Search_engine multi word search, order matters)
        """
        msg = 'Testing search_engine search order matters'
        result = self._student.search('dog tactics')
        expected = ['test_corpus/document2.txt', 'test_corpus/nsa.txt']
        self.assertEqual(expected, result, msg)

    def test_p2_search_multi_word_hard_long(self):
        """
        # name([Behavior: Common Case] SE9: Search_engine multi word search on instructor directory,
        # order matters, mixed case and punctuation)
        """
        msg = 'Testing search_engine search, order matters, mixed case and punctuation'
        term = 'sySTEMs t...ac!!tics'
        result = self._student.search(term)
        expected = ['test_corpus/document2.txt', 'test_corpus/nsa.txt']
        self.assertEqual(expected, result, msg)
