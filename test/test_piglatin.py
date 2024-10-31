import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_constructor(self):
        translator = PigLatin("This is a phrase")
        self.assertEqual("This is a phrase", translator.get_phrase())