import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_constructor(self):
        translator = PigLatin("This is a phrase")
        self.assertEqual("This is a phrase", translator.get_phrase())

    def test_translate_empty_string(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_translate_starts_with_vowel_ends_with_y(self):
        translator = PigLatin("any")
        self.assertEqual("anynay", translator.translate())

    def test_translate_starts_with_vowel_ends_with_vowel(self):
        translator = PigLatin("apple")
        self.assertEqual("appleay", translator.translate())

    def test_translate_starts_with_vowel_ends_with_consonant(self):
        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())

    def test_translate_starts_with_consonant(self):
        translator = PigLatin("hello")
        self.assertEqual("ellohay", translator.translate())

    def test_translate_starts_with_many_consonants(self):
        translator = PigLatin("known")
        self.assertEqual("ownknay", translator.translate())

    def test_translate_many_words(self):
        translator = PigLatin("hello world")
        self.assertEqual("ellohay orldway", translator.translate())

    def test_translate_composite_word(self):
        translator = PigLatin("well-being")
        self.assertEqual("ellway-eingbay", translator.translate())