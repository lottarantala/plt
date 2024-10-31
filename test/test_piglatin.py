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