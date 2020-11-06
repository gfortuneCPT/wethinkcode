from sys import stdout,stdin
import  unittest
from word_processor import *




class   Testword_processor(unittest.TestCase):

    def test_convert_to_word_list_punctuation(self):
        """Test sentence with punctuation and Upper case"""
        word_list = convert_to_word_list("Test, words? convert list")
        self.assertEqual(word_list, ["test", "words", "convert", "list"])
    
    def test_convert_to_word_list_empty_spaces(self):
        """Test extra spaces and empty string handling"""
        word_list = convert_to_word_list("Test, words?      convert list")
        self.assertEqual(word_list, ["test", "words", "convert", "list"])
        word_list = convert_to_word_list("")
        self.assertEqual(word_list, [])

    
    def test_words_longer_than(self):
        """Test correct retun of length of words larger than length"""

        text = "one two three four longer worrrrrrrd"
        self.assertEqual(words_longer_than(3, text), ["three", "four", "longer", "worrrrrrrd"])

    
    def test_word_length_map(self):
        """Test correct return of dict of word length"""

        text = "one two three four longer worrrrrrrd thf fhgd"
        self.assertEqual(words_lengths_map(text), {3: 3, 4: 2, 5: 1, 6: 1, 10: 1})

    
    def test_count_letter_map(self):
        """Test return of value for occurance of each letter"""

        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        self.assertEqual(letters_count_map(text), {'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0,
         'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0,
         'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0})


    def test_most_used_character(self):
        """Test correct return of key with highest occurance and empty string"""

        text = "one two three four longer worrrrrrrd thf fhgd"
        self.assertEqual(most_used_character(text), "r")
        text = ""
        self.assertEqual(most_used_character(text), None)