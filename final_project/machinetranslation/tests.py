import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english_null_input(self):
        actual = frenchToEnglish('null')
        expected = "NameError: name 'null' is not defined"
        self.assertEqual(actual, expected)