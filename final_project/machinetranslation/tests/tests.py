import unittest

from machinetranslation.translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english_null_input(self):
        self.assertEqual(french_to_english(' ')," ")
    def test_french_to_english_null_fail(self):
        self.assertNotEqual(french_to_english(' '),"a")
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),"Hello")

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french_null_input(self):
        self.assertEqual(english_to_french(' ')," ")
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),"Bonjour")
    def test_english_to_french_fail(self):
        self.assertNotEqual(english_to_french('Hello'),"Hello")

unittest.main()